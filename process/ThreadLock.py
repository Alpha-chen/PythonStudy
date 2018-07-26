#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'多线程锁的问题'
__author__ = 'click'
__date__ = '2018/7/24 下午3:46'

import time, threading

'出现多线程数据混乱的问题:线程之间共享创建的全局变量' \
'多进程之间的变量:进程间相互独立的,不存在多进程操作同一变量' \
'多线程:共享同一变量，存在多线程对同一变量操作的情况'

#####################################
'多线程造成变量数据改变的原因' \
'原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：'
'balance = balance + n'
'也分两步：'

'计算balance + n，存入临时变量中；'
'将临时变量的值赋给balance。'
'也就是可以看成：'

'x = balance + n'
'balance = x' \
    ####################################
'使用线程锁,对操作变量的方法进行加锁,保证变量值发生改变时只有一个线程对其操作。单线程的模式'

balance = 0

# 初始化一个锁
# lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        # 1.首先申请锁
        # lock.acquire()
        # try:
            change_it(n)
        # finally:
            # 使用try  finaly 保证执行完之后，释放锁
            # lock.release()


t1 = threading.Thread(target=run_thread, args=(4,))
t2 = threading.Thread(target=run_thread, args=(6,))

t1.start()
t2.start()
t1.join()
t2.join()
print('balance %s' % balance)
