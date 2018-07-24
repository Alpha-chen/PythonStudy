#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'爆满CPU的死亡代码'
'如果你的女票肚子不舒服，你也可以用这段代码给她暖暖' \
'呵，单身狗想的真美好'

__author__ = 'click'
__date__ = '2018/7/24 下午4:19'

import multiprocessing, threading


def loop():
    x = 0
    while True:
        x = x ^ 1
        print('%1s->%2s' % (threading.current_thread().name, x))


for i in range(multiprocessing.cpu_count()):
    threading = threading.Thread(target=loop, args=('死亡loop'))
    threading.start()
