#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'多线程'
__author__ = 'click'
__date__ = '2018/7/23 下午6:20'

import time, threading


def threadReadFile():
    print('主线程的名字%s' % threading.current_thread().name)
    # print('读取文件中内容是%s' % myio.ReadAndWrite.readTxt())
    n = 0
    while n < 10:
        n = n + 1

    print('执行相加操作结果是%s' % n)


t = threading.Thread(target=threadReadFile, name='threadReadFile')
t.start()
t.join()
print("当前线城是%s" % threading.current_thread().name)
