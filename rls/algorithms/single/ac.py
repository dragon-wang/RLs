#!/usr/bin/env python3
# encoding: utf-8

import numpy as np
import torch as t

from torch import distributions as td
from dataclasses import dataclass

from rls.utils.torch_utils import q_target_func
from rls.algorithms.base.off_policy import Off_Policy
from rls.common.specs import BatchExperiences
from rls.nn.models import (ActorMuLogstd,
                           ActorDct,
                           CriticQvalueOne)
from rls.nn.utils import OPLR
from rls.common.decorator import iTensor_oNumpy


@dataclass(eq=False)
class AC_BatchExperiences(BatchExperiences):
    old_log_prob: np.ndarray


class AC(Off_Policy):
    # off-policy actor-critic
    def __init__(self,
                 envspec,

                 actor_lr=5.0e-4,
                 critic_lr=1.0e-3,
                 network_settings={
                     'actor_continuous': {
                         'hidden_units': [64, 64],
                         'condition_sigma': False,
                         'log_std_bound': [-20, 2]
                     },
                     'actor_discrete': [32, 32],
                     'critic': [32, 32]
                 },
                 **kwargs):
        super().__init__(envspec=envspec, **kwargs)

        if self.is_continuous:
            self.actor = ActorMuLogstd(self.rep_net.h_dim,
                                       output_shape=self.a_dim,
                                       network_settings=network_settings['actor_continuous']).to(self.device)
        else:
            self.actor = ActorDct(self.rep_net.h_dim,
                                  output_shape=self.a_dim,
                                  network_settings=network_settings['actor_discrete']).to(self.device)
        self.critic = CriticQvalueOne(self.rep_net.h_dim,
                                      action_dim=self.a_dim,
                                      network_settings=network_settings['critic']).to(self.device)

        self.actor_oplr = OPLR(self.actor, actor_lr)
        self.critic_oplr = OPLR([self.critic, self.rep_net], critic_lr)

        self._worker_modules.update(rep_net=self.rep_net,
                                    actor=self.actor)

        self._trainer_modules.update(self._worker_modules)
        self._trainer_modules.update(critic=self.critic,
                                     actor_oplr=self.actor_oplr,
                                     critic_oplr=self.critic_oplr)
        self.initialize_data_buffer()

    def __call__(self, obs, evaluation=False):
        """
        choose an action according to a given observation
        :param obs: 
        :param evaluation:
        """
        actions, self.cell_state, self._log_prob = self.call(obs, cell_state=self.cell_state)

    @iTensor_oNumpy
    def call(self, obs, cell_state):
        feat, cell_state = self.rep_net(obs, cell_state=cell_state)
        output = self.actor(feat)
        if self.is_continuous:
            mu, log_std = output
            dist = td.Independent(td.Normal(mu, log_std.exp()), 1)
            sample_op = dist.sample().clamp(-1, 1)
            log_prob = dist.log_prob(sample_op).unsqueeze(-1)
        else:
            logits = output
            norm_dist = td.Categorical(logits=logits)
            sample_op = norm_dist.sample()
            log_prob = norm_dist.log_prob(sample_op)
        return sample_op, cell_state, log_prob

    def store_data(self, exps: BatchExperiences):
        # self._running_average()
        self.data.add(AC_BatchExperiences(*exps.astuple(), self._log_prob))

    def prefill_store(self, exps: BatchExperiences):
        # self._running_average()
        self.data.add(AC_BatchExperiences(*exps.astuple(), np.ones_like(exps.reward)))

    def learn(self, **kwargs):
        self.train_step = kwargs.get('train_step')
        for i in range(self.train_times_per_step):
            self._learn(function_dict={
                'summary_dict': dict([
                    ['LEARNING_RATE/actor_lr', self.actor_oplr.lr],
                    ['LEARNING_RATE/critic_lr', self.critic_oplr.lr]
                ])
            })

    @iTensor_oNumpy
    def _train(self, BATCH, isw, cell_states):
        feat, _ = self.rep_net(BATCH.obs, cell_state=cell_states['obs'])
        feat_, _ = self.rep_net(BATCH.obs_, cell_state=cell_states['obs_'])
        q = self.critic(feat)
        if self.is_continuous:
            next_mu, _ = self.actor(feat_)
            max_q_next = self.critic(feat_, next_mu).detach()
        else:
            logits = self.actor(feat_)
            max_a = logits.argmax(1)
            max_a_one_hot = t.nn.functional.one_hot(max_a, self.a_dim).float()
            max_q_next = self.critic(feat_, max_a_one_hot).detach()
        q_value = q.detach()
        td_error = q - q_target_func(BATCH.reward,
                                     self.gamma,
                                     BATCH.done,
                                     max_q_next)
        critic_loss = (td_error.square() * isw).mean()
        self.critic_oplr.step(critic_loss)

        feat = feat.detach()
        q_value = q.detach()
        if self.is_continuous:
            mu, log_std = self.actor(feat)
            dist = td.Independent(td.Normal(mu, log_std.exp()), 1)
            log_prob = dist.log_prob(BATCH.action).unsqueeze(-1)
            entropy = dist.entropy().mean()
        else:
            logits = self.actor(feat)
            logp_all = logits.log_softmax(-1)
            log_prob = (logp_all * BATCH.action).sum(1, keepdim=True)
            entropy = -(logp_all.exp() * logp_all).sum(1, keepdim=True).mean()
        ratio = (log_prob - BATCH.old_log_prob).exp().detach()
        actor_loss = -(ratio * log_prob * q_value).mean()
        self.actor_oplr.step(actor_loss)

        self.global_step.add_(1)
        return td_error, dict([
            ['LOSS/actor_loss', actor_loss],
            ['LOSS/critic_loss', critic_loss],
            ['Statistics/q_max', q.max()],
            ['Statistics/q_min', q.min()],
            ['Statistics/q_mean', q.mean()],
            ['Statistics/ratio', ratio.mean()],
            ['Statistics/entropy', entropy]
        ])
