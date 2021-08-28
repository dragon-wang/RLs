#!/usr/bin/env python3
# encoding: utf-8

import os
from collections import defaultdict
from copy import deepcopy
from typing import Dict, List

import numpy as np
from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.side_channel.engine_configuration_channel import \
    EngineConfigurationChannel
from mlagents_envs.side_channel.environment_parameters_channel import \
    EnvironmentParametersChannel

from rls.common.specs import Data, EnvAgentSpec, SensorSpec
from rls.common.yaml_ops import load_config
from rls.envs.unity.wrappers.core import ActionWrapper, ObservationWrapper
from rls.utils.np_utils import get_discrete_action_list


class BasicUnityEnvironment(object):

    def __init__(self,
                 worker_id=0,
                 file_name=None,
                 port=5005,
                 render=False,
                 seed=42,
                 timeout_wait=60,
                 env_copys=12,
                 env_name='3DBall',
                 real_done=True,
                 initialize_config={},
                 engine_config={
                     'width': 84,
                     'height': 84,
                     'quality_level': 5,
                     'time_scale': 20,
                     'target_frame_rate': -1,
                     'capture_frame_rate': 60
                 },
                 **kwargs):
        self._n_copys = env_copys
        self._real_done = real_done

        self._side_channels = self.initialize_all_side_channels(
            initialize_config, engine_config)
        env_kwargs = dict(seed=seed,
                          worker_id=worker_id,
                          timeout_wait=timeout_wait,
                          side_channels=list(self._side_channels.values()))    # 注册所有初始化后的通讯频道
        if file_name is not None:
            env_dict = load_config('rls/configs/unity/env_dict.yaml')
            env_kwargs.update(file_name=file_name,
                              base_port=port,
                              no_graphics=not render,
                              additional_args=[
                                  '--scene', str(env_dict.get(env_name, 'None'))
                              ])
        self.env = UnityEnvironment(**env_kwargs)
        self.env.reset()
        self.initialize_environment()

    def initialize_all_side_channels(self, initialize_config, engine_config):
        '''
        初始化所有的通讯频道
        '''
        engine_configuration_channel = EngineConfigurationChannel()
        engine_configuration_channel.set_configuration_parameters(
            **engine_config)
        float_properties_channel = EnvironmentParametersChannel()
        float_properties_channel.set_float_parameter(
            'env_copys', self._n_copys)
        for k, v in initialize_config.items():
            float_properties_channel.set_float_parameter(k, v)
        return dict(engine_configuration_channel=engine_configuration_channel,
                    float_properties_channel=float_properties_channel)

    def initialize_environment(self):
        '''
        初始化环境，获取必要的信息，如状态、动作维度等等
        '''

        self.behavior_names = list(self.env.behavior_specs.keys())

        self._vector_idxs = defaultdict(list)
        self._vector_dims = defaultdict(list)
        self._visual_idxs = defaultdict(list)
        self._visual_dims = defaultdict(list)
        self._a_dim = defaultdict(int)
        self._discrete_action_lists = {}
        self._is_continuous = {}
        self._actiontuples = {}

        self.env.reset()
        for bn, spec in self.env.behavior_specs.items():
            for i, obs_spec in enumerate(spec.observation_specs):   # TODO: optimize
                if len(obs_spec.shape) == 1:
                    self._vector_idxs[bn].append(i)
                    self._vector_dims[bn].append(obs_spec.shape[0])
                elif len(obs_spec.shape) == 3:
                    self._visual_idxs[bn].append(i)
                    self._visual_dims[bn].append(list(obs_spec.shape))
                else:
                    raise ValueError(
                        "shape of observation cannot be understood.")

            action_spec = spec.action_spec
            if action_spec.is_continuous():
                self._a_dim[bn] = action_spec.continuous_size
                self._discrete_action_lists[bn] = None
                self._is_continuous[bn] = True
            elif action_spec.is_discrete():
                self._a_dim[bn] = int(np.asarray(
                    action_spec.discrete_branches).prod())
                self._discrete_action_lists[bn] = get_discrete_action_list(
                    action_spec.discrete_branches)
                self._is_continuous[bn] = False
            else:
                raise NotImplementedError(
                    "doesn't support continuous and discrete actions simultaneously for now.")

            self._actiontuples[bn] = action_spec.empty_action(
                n_agents=self._n_copys)

    def reset(self, reset_config):
        for k, v in reset_config.items():
            self._side_channels['float_properties_channel'].set_float_parameter(
                k, v)
        self.env.reset()
        return self.get_obs(only_obs=True)

    def step(self, actions, step_config):
        '''
        params: actions, type of dict or np.ndarray, if the type of actions is
                not dict, then set those actions for the first behavior controller.
        '''
        for k, v in step_config.items():
            self._side_channels['float_properties_channel'].set_float_parameter(
                k, v)

        actions = deepcopy(actions)

        # TODO: fix this
        for bn in self.behavior_names:
            if self._is_continuous[bn]:
                self._actiontuples[bn].add_continuous(actions[bn])
            else:
                self._actiontuples[bn].add_discrete(
                    self._discrete_action_lists[bn][actions[bn]].reshape(self._n_copys, -1))
            self.env.set_actions(bn, self._actiontuples[bn])

        self.env.step()
        return self.get_obs()

    @property
    def AgentSpecs(self):
        ret = {}
        for bn in self.behavior_names:
            ret[bn] = EnvAgentSpec(
                obs_spec=SensorSpec(
                    vector_dims=self._vector_dims[bn],
                    visual_dims=self._visual_dims[bn]),
                a_dim=self._a_dim[bn],
                is_continuous=self._is_continuous[bn]
            )
        return ret

    @property
    def StateSpec(self) -> SensorSpec:
        return SensorSpec()

    @property
    def agent_ids(self) -> List[str]:
        return self.behavior_names

    def get_obs(self, behavior_names=None, only_obs=False):
        '''
        解析环境反馈的信息，将反馈信息分为四部分：向量、图像、奖励、done信号
        '''
        behavior_names = behavior_names or self.behavior_names

        whole_done = np.full(self._n_copys, False)
        whole_info_max_step = np.full(self._n_copys, False)
        all_obs = {}
        all_reward = {}

        for bn in behavior_names:
            ps = []

            # TODO: optimize
            while True:
                ds, ts = self.env.get_steps(bn)
                if len(ts):
                    ps.append(ts)
                if len(ds) == self._n_copys:
                    break
                elif len(ds) == 0:
                    self.env.step()  # some of environments done, but some of not
                else:
                    raise ValueError(
                        f'agents number error. Expected 0 or {self._n_copys}, received {len(ds)}')

            obs, reward = ds.obs, ds.reward
            done = np.full(self._n_copys, False)
            begin_mask = np.full(self._n_copys, False)
            info_max_step = np.full(self._n_copys, False)
            info_real_done = np.full(self._n_copys, False)

            for ts in ps:    # TODO: 有待优化
                _ids = ts.agent_id
                reward[_ids] = ts.reward
                info_max_step[_ids] = ts.interrupted    # 因为达到episode最大步数而终止的
                # 去掉因为max_step而done的，只记录因为失败/成功而done的
                info_real_done[_ids[~ts.interrupted]] = True
                done[_ids] = True
                begin_mask[_ids] = True
                # zip: vector, visual, ...
                for _obs, _tobs in zip(obs, ts.obs):
                    _obs[_ids] = _tobs

            if self._real_done:
                done = np.array(info_real_done)

            _obs = Data()
            if len(self._vector_idxs[bn]) > 0:
                _obs.update(
                    vector={f'vector_{i}': obs[vi] for i, vi in enumerate(self._vector_idxs[bn])})

            if len(self._visual_idxs[bn]) > 0:
                _obs.update(
                    visual={f'visual_{i}': obs[vi] for i, vi in enumerate(self._visual_idxs[bn])})
            all_obs[bn] = _obs
            all_reward[bn] = reward

        whole_done = np.logical_or(whole_done, done)
        whole_info_max_step = np.logical_or(whole_info_max_step, info_max_step)

        if only_obs:
            all_obs.update(
                {'global': Data(begin_mask=np.full((self._n_copys, 1), True))})
            return all_obs
        else:
            rets = {}
            for bn in self.behavior_names:
                rets[bn] = Data(obs=all_obs[bn],
                                reward=all_reward[bn],
                                done=whole_done,
                                info=dict(max_step=whole_info_max_step))
            rets.update(
                {'global': Data(begin_mask=begin_mask[:, np.newaxis])})  # [B, 1]
            return rets

    def __getattr__(self, name):
        '''
        不允许获取BasicUnityEnvironment中以'_'开头的属性
        '''
        if name.startswith('_'):
            raise AttributeError(
                "attempted to get missing private attribute '{}'".format(name))
        return getattr(self.env, name)


class ScaleVisualWrapper(ObservationWrapper):

    def observation(self, observation: Dict[str, Data]):

        def func(x): return np.asarray(x * 255).astype(np.uint8)

        for k in observation.keys():
            observation[k].obs.visual.convert_(func)
            observation[k].obs_.visual.convert_(func)
        return observation