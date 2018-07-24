#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'进程间通信'
'Process之间肯定是需要通信的，' \
'操作系统提供了很多机制来实现进程间的通信。' \
'Python的multiprocessing模块包装了底层的机制，' \
'提供了Queue、Pipes等多种方式来交换数据。'
__author__ = 'click'
__date__ = '2018/7/23 下午5:29'

from multiprocessing import Process, Queue

import time, random, os


# 网队列中写操作
def write(queue):
    print('队列的写入操作')

    for x in ['A', 'B', 'c']:
        print('插入的内容是%s' % (x))
        queue.put(x)
        time.sleep(random.random())


# 读操作

def read(queue):
    print('队列的读操作')
    # 这里要循环从队列中读取
    while True:
        s = queue.get(True)
        print('队列中读取的内容是%s' % (s))


if __name__ == '__main__':
    # 创建一个queue
    q = Queue()
    # 创建一个写操作的进程
    pw = Process(target=write, args=(q,))
    # 创建一个读操作的进程
    pr = Process(target=read, args=(q,))
    # 启动进程
    pw.start()
    pr.start()
    # 进入到
    pw.join()
    pr.terminate()
