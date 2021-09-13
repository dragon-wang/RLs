#!/usr/bin/env python3
# encoding: utf-8

from rls.algorithms.register import get_model_info, register

# logo: font-size: 12, foreground character: 'O', font: 幼圆
# http://life.chacuo.net/convertfont2char

register(   # font 8
    name='maddpg',
    path='multi.maddpg',
    is_multi=True,
    class_name='MADDPG',
    logo='''
　　　　　　　　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　ＯＯＯＯＯ　　
　ＯＯＯＯ　　　ＯＯＯＯ　　　　　　ＯＯ　　　　　　ＯＯＯＯＯＯＯＯ　　　　ＯＯＯＯＯＯＯＯ　　　　　ＯＯＯＯＯＯＯ　　　　　ＯＯＯＯＯＯＯ　　
　　　ＯＯＯ　　ＯＯＯ　　　　　　ＯＯＯＯ　　　　　　ＯＯ　　ＯＯＯ　　　　　ＯＯ　　ＯＯＯ　　　　　　ＯＯ　　ＯＯ　　　　　ＯＯＯ　　　Ｏ　　
　　　ＯＯＯ　ＯＯＯＯ　　　　　　ＯＯＯＯ　　　　　　ＯＯ　　　ＯＯＯ　　　　ＯＯ　　　ＯＯＯ　　　　　ＯＯ　　ＯＯ　　　　ＯＯＯ　　　　　　　
　　　ＯＯＯＯＯＯＯＯ　　　　　　Ｏ　ＯＯ　　　　　　ＯＯ　　　　ＯＯ　　　　ＯＯ　　　　ＯＯ　　　　　ＯＯＯＯＯＯ　　　　ＯＯＯ　　　ＯＯＯ　
　　　Ｏ　ＯＯＯ　ＯＯ　　　　　ＯＯＯＯＯＯ　　　　　ＯＯ　　　　ＯＯ　　　　ＯＯ　　　　ＯＯ　　　　　ＯＯ　　　　　　　　ＯＯＯ　　　ＯＯ　　
　　　Ｏ　ＯＯＯ　ＯＯ　　　　　ＯＯ　　ＯＯ　　　　　ＯＯ　　　ＯＯＯ　　　　ＯＯ　　　ＯＯＯ　　　　　ＯＯ　　　　　　　　　ＯＯＯ　　ＯＯ　　
　　ＯＯＯＯＯ　ＯＯＯ　　　　ＯＯ　　　ＯＯＯ　　　　ＯＯＯＯＯＯＯ　　　　　ＯＯＯＯＯＯＯ　　　　　　ＯＯＯ　　　　　　　　ＯＯＯＯＯＯＯ　　
　ＯＯＯＯ　Ｏ　ＯＯＯ　　　　ＯＯ　　　ＯＯＯ　　　ＯＯＯＯＯＯＯ　　　　　ＯＯＯＯＯＯＯ　　　　　　ＯＯＯＯ　　　　　　　　　　ＯＯＯＯ
    '''
)

register(   # font 8
    name='masac',
    path='multi.masac',
    is_multi=True,
    class_name='MASAC',
    logo='''
　　　　　　　　　　　　　　　　　　ＯＯ　　　　　　　　　ＯＯＯＯ　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　　
　ＯＯＯＯ　　　ＯＯＯＯ　　　　　　ＯＯ　　　　　　　　ＯＯＯＯＯ　　　　　　　　　ＯＯ　　　　　　　　ＯＯＯＯＯＯ　　
　　　ＯＯＯ　　ＯＯＯ　　　　　　ＯＯＯＯ　　　　　　　ＯＯ　ＯＯ　　　　　　　　ＯＯＯＯ　　　　　　ＯＯＯ　　ＯＯ　　
　　　ＯＯＯ　ＯＯＯＯ　　　　　　ＯＯＯＯ　　　　　　　ＯＯＯ　　　　　　　　　　ＯＯＯＯ　　　　　　ＯＯ　　　　Ｏ　　
　　　ＯＯＯＯＯＯＯＯ　　　　　　Ｏ　ＯＯ　　　　　　　ＯＯＯＯＯ　　　　　　　　Ｏ　ＯＯ　　　　　ＯＯＯ　　　　　　　
　　　Ｏ　ＯＯＯ　ＯＯ　　　　　ＯＯＯＯＯＯ　　　　　　　　ＯＯＯ　　　　　　　ＯＯＯＯＯＯ　　　　ＯＯＯ　　　　　　　
　　　Ｏ　ＯＯＯ　ＯＯ　　　　　ＯＯ　　ＯＯ　　　　　　Ｏ　　ＯＯ　　　　　　　ＯＯ　　ＯＯ　　　　　ＯＯ　　　　　　　
　　ＯＯＯＯＯ　ＯＯＯ　　　　ＯＯ　　　ＯＯＯ　　　　　ＯＯＯＯＯ　　　　　　ＯＯ　　　ＯＯＯ　　　　ＯＯＯＯ　ＯＯ　　
　ＯＯＯＯ　Ｏ　ＯＯＯ　　　　ＯＯ　　　ＯＯＯ　　　　　ＯＯＯＯＯ　　　　　　ＯＯ　　　ＯＯＯ　　　　　ＯＯＯＯＯ
    '''
)

register(
    name='vdn',
    path='multi.vdn',
    is_multi=True,
    class_name='VDN',
    logo='''
　　　　ＯＯＯＯＯ　　　ＯＯＯＯ　　　　　ＯＯＯＯＯＯＯＯＯＯ　　　　　　　ＯＯＯＯＯ　　　　ＯＯＯＯ　　　
　　　　ＯＯＯＯＯ　　　ＯＯＯＯ　　　　　　ＯＯＯＯＯＯＯＯＯＯ　　　　　　　　ＯＯＯＯ　　　　ＯＯ　　　　
　　　　　ＯＯＯ　　　　ＯＯ　　　　　　　　　ＯＯ　　　　ＯＯＯＯ　　　　　　　　ＯＯＯＯ　　　　Ｏ　　　　
　　　　　　ＯＯＯ　　　ＯＯ　　　　　　　　　ＯＯ　　　　　ＯＯＯＯ　　　　　　　ＯＯＯＯＯ　　　Ｏ　　　　
　　　　　　ＯＯＯ　　ＯＯＯ　　　　　　　　　ＯＯ　　　　　ＯＯＯＯ　　　　　　　Ｏ　ＯＯＯＯ　　Ｏ　　　　
　　　　　　ＯＯＯ　　ＯＯ　　　　　　　　　　ＯＯ　　　　　　ＯＯＯ　　　　　　　Ｏ　　ＯＯＯＯ　Ｏ　　　　
　　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　ＯＯ　　　　　　ＯＯＯ　　　　　　　Ｏ　　ＯＯＯＯＯＯ　　　　
　　　　　　　ＯＯＯＯＯ　　　　　　　　　　　ＯＯ　　　　　ＯＯＯＯ　　　　　　　Ｏ　　　ＯＯＯＯＯ　　　　
　　　　　　　　ＯＯＯＯ　　　　　　　　　　　ＯＯ　　　　　ＯＯＯ　　　　　　　　Ｏ　　　　ＯＯＯＯ　　　　
　　　　　　　　ＯＯＯ　　　　　　　　　　　　ＯＯ　　　ＯＯＯＯＯ　　　　　　　　Ｏ　　　　　ＯＯＯ　　　　
　　　　　　　　　ＯＯ　　　　　　　　　　ＯＯＯＯＯＯＯＯＯＯＯ　　　　　　　ＯＯＯＯ　　　　　ＯＯ　　　　
　　　　　　　　　ＯＯ
    '''
)

register(
    name='qmix',
    path='multi.vdn',
    is_multi=True,
    class_name='VDN',
    logo='''
　　　　　　ＯＯＯＯＯＯ　　　　　　　　ＯＯＯＯ　　　　　　ＯＯＯＯ　　　　　　　　ＯＯＯＯＯ　　　　　　　　　　ＯＯＯＯＯＯ　　ＯＯＯＯ　　　
　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　　ＯＯＯＯ　　　　　ＯＯＯＯ　　　　　　　　　ＯＯＯ　　　　　　　　　　　　　ＯＯＯＯ　　　ＯＯ　　　　
　　　　ＯＯＯＯ　　　ＯＯＯ　　　　　　　　ＯＯＯ　　　　ＯＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯＯＯ　　ＯＯＯ　　　　
　　　　ＯＯＯ　　　　ＯＯＯＯ　　　　　　　ＯＯＯＯ　　　ＯＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　ＯＯＯＯＯＯＯ　　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　ＯＯＯＯ　　ＯＯＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯＯＯＯ　　　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　Ｏ　ＯＯＯ　ＯＯ　ＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　　ＯＯＯＯ　　　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　Ｏ　ＯＯＯＯＯＯ　ＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯＯＯＯＯ　　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　Ｏ　ＯＯＯＯＯ　　ＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　ＯＯＯＯＯＯＯ　　　　　
　　　　ＯＯＯ　　　　　ＯＯＯ　　　　　　　Ｏ　　ＯＯＯＯ　　ＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　ＯＯ　　ＯＯＯＯ　　　　
　　　　ＯＯＯＯ　　　ＯＯＯ　　　　　　　　Ｏ　　ＯＯＯ　　　ＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　　　ＯＯＯＯＯ　　　
　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　ＯＯＯＯ　　ＯＯ　ＯＯＯＯＯＯ　　　　　　　ＯＯＯＯＯ　　　　　　　　　　ＯＯＯＯ　　　　ＯＯＯＯＯ　　
　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
　　　　　　　　ＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
　　　　　　　　　　ＯＯＯＯ
    '''
)

register(   # font-10
    name='qatten',
    path='multi.vdn',
    is_multi=True,
    class_name='VDN',
    logo='''
　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　ＯＯＯＯＯＯＯＯ　　　　　　ＯＯＯＯ　　　ＯＯＯＯ　　
　　　　ＯＯＯ　ＯＯＯＯ　　　　　　　　　ＯＯＯ　　　　　　　　　ＯＯ　　ＯＯ　ＯＯ　　　　　　ＯＯ　　ＯＯ　ＯＯ　　　　　　　ＯＯＯ　　ＯＯ　　　　　　　　ＯＯＯ　　　　Ｏ　　　
　　　ＯＯＯ　　　ＯＯＯＯ　　　　　　　　ＯＯＯＯ　　　　　　　　Ｏ　　　ＯＯ　　Ｏ　　　　　　Ｏ　　　ＯＯ　　Ｏ　　　　　　　ＯＯＯ　　　Ｏ　　　　　　　　ＯＯＯＯ　　　Ｏ　　　
　　　ＯＯＯ　　　　ＯＯＯ　　　　　　　　ＯＯＯＯ　　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　　　　　　　　　　ＯＯＯ　　Ｏ　　　　　　　　　ＯＯＯＯＯ　　Ｏ　　　
　　　ＯＯ　　　　　ＯＯＯ　　　　　　　ＯＯ　ＯＯ　　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　　　　　　　　　　ＯＯＯＯＯＯ　　　　　　　　　Ｏ　ＯＯＯＯ　Ｏ　　　
　　　ＯＯＯ　　　　ＯＯＯ　　　　　　　ＯＯ　ＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　　　　　　　　　　ＯＯＯ　　Ｏ　　　　　　　　　Ｏ　　ＯＯＯＯＯ　　　
　　　ＯＯＯ　　　　ＯＯＯ　　　　　　ＯＯＯＯＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　　　　　　　　　　ＯＯＯ　　Ｏ　Ｏ　　　　　　　Ｏ　　　ＯＯＯＯ　　　
　　　ＯＯＯ　　　ＯＯＯ　　　　　　　ＯＯ　　　ＯＯＯ　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　　　　　　　　　　ＯＯＯ　　　ＯＯ　　　　　　　Ｏ　　　　ＯＯＯ　　　
　　　　ＯＯＯＯＯＯＯＯ　　　　　　ＯＯＯ　　　ＯＯＯ　　　　　　　　ＯＯＯＯＯ　　　　　　　　　　ＯＯＯＯＯ　　　　　　　　ＯＯＯＯＯＯＯＯ　　　　　　　ＯＯＯ　　　　ＯＯ　　　
　　　　　ＯＯＯＯＯ　　　　　　　　ＯＯＯ　　　ＯＯＯＯ　　　　　　　ＯＯＯＯＯ　　　　　　　　　　ＯＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
　　　　　　　ＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
　　　　　　　　　ＯＯＯ
    '''
)

register(
    name='qtran',
    path='multi.qtran',
    is_multi=True,
    class_name='QTRAN',
    logo='''
　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　　　　　　　　　ＯＯ　　　　　　　　　　ＯＯＯＯＯ　　　　ＯＯＯＯ　　　
　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　　　ＯＯＯＯＯＯＯＯＯＯ　　　　　　　　　ＯＯＯＯＯＯＯＯ　　　　　　　　　　　　ＯＯＯ　　　　　　　　　　　　ＯＯＯＯ　　　　ＯＯ　　　　
　　　　ＯＯＯＯ　　　ＯＯＯ　　　　　　　　ＯＯ　　ＯＯ　　ＯＯ　　　　　　　　　ＯＯ　　　ＯＯＯ　　　　　　　　　　　　ＯＯＯ　　　　　　　　　　　　　ＯＯＯＯ　　　　Ｏ　　　　
　　　　ＯＯＯ　　　　ＯＯＯＯ　　　　　　　Ｏ　　　ＯＯ　　　Ｏ　　　　　　　　　ＯＯ　　　ＯＯＯ　　　　　　　　　　　ＯＯＯＯＯ　　　　　　　　　　　　ＯＯＯＯＯ　　　Ｏ　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　　　ＯＯＯ　　　　　　　　　　　ＯＯＯＯＯ　　　　　　　　　　　　Ｏ　ＯＯＯＯ　　Ｏ　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　ＯＯＯＯ　　　　　　　　　　　　ＯＯ　ＯＯＯ　　　　　　　　　　　Ｏ　　ＯＯＯＯ　Ｏ　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯＯＯＯＯＯ　　　　　　　　　　　ＯＯ　　ＯＯＯ　　　　　　　　　　　Ｏ　　ＯＯＯＯＯＯ　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　　ＯＯＯＯＯＯＯＯ　　　　　　　　　　Ｏ　　　ＯＯＯＯＯ　　　　
　　　　ＯＯＯ　　　　　ＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　ＯＯＯＯ　　　　　　　　　　ＯＯＯ　　　ＯＯＯ　　　　　　　　　　Ｏ　　　　ＯＯＯＯ　　　　
　　　　ＯＯＯＯ　　　ＯＯＯ　　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　ＯＯ　　ＯＯＯＯ　　　　　　　　　ＯＯ　　　　ＯＯＯ　　　　　　　　　　Ｏ　　　　　ＯＯＯ　　　　
　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　　　　　　　ＯＯＯ　　　　　　　　　　　　ＯＯＯ　　ＯＯＯＯ　　　　　　　ＯＯＯ　　　　ＯＯＯＯ　　　　　　　ＯＯＯＯ　　　　　ＯＯ　　　　
　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　　ＯＯＯＯＯＯ　　　　　　　　　ＯＯＯＯＯＯ　　ＯＯＯＯ　　　　　　ＯＯＯ　　　　ＯＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　
　　　　　　　　ＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
　　　　　　　　　　ＯＯＯＯ
    '''
)

register(
    name='qplex',
    path='multi.qplex',
    is_multi=True,
    class_name='QPLEX',
    logo='''
　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　ＯＯＯＯＯＯＯＯ　　　　　　　　　ＯＯＯＯＯ　　　　　　　　　　　　ＯＯＯＯＯＯＯＯＯＯ　　　　　　　　ＯＯＯＯＯＯ　　ＯＯＯＯ　　　
　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　　　　　ＯＯＯＯＯＯＯＯ　　　　　　　　　ＯＯＯ　　　　　　　　　　　　　　ＯＯＯ　　　ＯＯＯ　　　　　　　　　　ＯＯＯＯ　　　ＯＯ　　　　
　　　　ＯＯＯＯ　　　ＯＯＯ　　　　　　　　　　　ＯＯ　　ＯＯＯＯ　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯ　　　　ＯＯ　　　　　　　　　　ＯＯＯＯ　　ＯＯＯ　　　　
　　　　ＯＯＯ　　　　ＯＯＯＯ　　　　　　　　　　ＯＯ　　　ＯＯＯ　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯ　　　　　Ｏ　　　　　　　　　　　ＯＯＯＯＯＯＯ　　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　　　　ＯＯ　　ＯＯＯＯ　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯ　　　ＯＯ　　　　　　　　　　　　　ＯＯＯＯＯ　　　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　　　　ＯＯＯＯＯＯＯ　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯＯＯＯＯＯ　　　　　　　　　　　　　　ＯＯＯＯ　　　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯ　　　ＯＯ　　　　　　　　　　　　　ＯＯＯＯＯＯ　　　　　
　　　ＯＯＯ　　　　　　ＯＯＯ　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯ　　　　Ｏ　　　　　　　　　　　　ＯＯＯＯＯＯＯ　　　　　
　　　　ＯＯＯ　　　　　ＯＯＯ　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯ　　　　　Ｏ　　　　　　　　　ＯＯ　　　　　ＯＯ　　　　　　　　　　ＯＯ　　ＯＯＯＯ　　　　
　　　　ＯＯＯＯ　　　ＯＯＯ　　　　　　　　　　　ＯＯ　　　　　　　　　　　　　　　ＯＯ　　　　ＯＯ　　　　　　　　　ＯＯＯ　　　ＯＯ　　　　　　　　　　ＯＯ　　　ＯＯＯＯＯ　　　
　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　ＯＯＯＯＯＯＯＯＯ　　　　　　　　ＯＯＯＯＯＯＯＯＯＯ　　　　　　　　ＯＯＯＯ　　　　ＯＯＯＯＯ　　
　　　　　　ＯＯＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
　　　　　　　　ＯＯＯＯ　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
　　　　　　　　　　ＯＯＯＯ
    '''
)
