#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

#
# _ooOoo_
# o8888888o
# 88" . "88
# (| -_- |)
#  O\ = /O
# ___/`---'\____
# .   ' \\| |// `.
# / \\||| : |||// \
# / _||||| -:- |||||- \
# | | \\\ - /// | |
# | \_| ''\---/'' | |
# \ .-\__ `-` ___/-. /
# ___`. .' /--.--\ `. . __
# ."" '< `.___\_<|>_/___.' >'"".
# | | : `- \`.;`\ _ /`;.`/ - ` : | |
# \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
# `=---='
# .............................................
#           佛曰：bug泛滥，我已瘫痪！
#

'生产进程'
__author__ = 'click'
__date__ = '2018/7/25 下午3:13'

import random, time, queue, sys
from multiprocessing.managers import BaseManager


# 创建BaseManager

class QueueManger(BaseManager):
    pass


# 向网络中注册生产,消费队列
QueueManger.register('get_master_queue')
QueueManger.register('get_worker_queue')

# 连接到服务器,也就是运行master_queue的机器

server_addr = '127.0.0.1'
print('连接到服务端 %s' % server_addr)
# 初始化manager
manager = QueueManger(address=(server_addr, 5000), authkey=b'abc')

# 连接到服务器
manager.connect()
# 获取到master队列
master = manager.get_master_queue()
# 获取到消费worker队列
worker = manager.get_worker_queue()

# 从master中获取任务,并放到worker队列中

for i in range(10):
    try:
        n = master.get(timeout=1)
        print('worker进程获取到master队列中的元素%s' % n)
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        worker.put(r)
    except queue.Empty:
        print('队列为空')
# 工作进程执行完毕
print('worker执行完成')
