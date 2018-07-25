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

'分布式进程,使用multiprocessing.manager模块进行多进程队列的管理'
__author__ = 'click'
__date__ = '2018/7/25 下午1:55'

import time, random, queue
from multiprocessing.managers import BaseManager

# 创建生产队列master
masterQueue = queue.Queue()
# 创建消费队列,worker

workerQueue = queue.Queue()


# 创建manager管理queue

class QueueManager(BaseManager):
    pass


# 使用baseManager将两个队列注册到网络上

QueueManager.register('get_master_queue', callable=lambda: masterQueue)
QueueManager.register('get_worker_queue', callable=lambda: workerQueue)

# 绑定网络端口5000,设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')

# 启动queue
manager.start()

# 获取到注册到网络上的生产、消费队列

master = manager.get_master_queue()

worker = manager.get_worker_queue()
# 往生产队列中添加任务

for i in range(10):
    n = random.randint(0, 10)
    print('往master队列中添加任务 %s' % n)
    master.put(n)

# 准备从消费队列中取出
print('从消费队列获取内容')

for i in range(10):
    r = worker.get(timeout=10)
    print('消费队列worker%s' % r)

# 关闭manger
manager.shutdown()
