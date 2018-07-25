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

'多线程变量优化,单个线程只是用当前线程的变量'
'一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本' \
'，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。'
__author__ = 'click'
__date__ = '2018/7/24 下午5:44'

import threading

threadLocal = threading.local()


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student的属性__name的值是 %s' % (self.__name)
        # 直接使用str会打印出该对象的内存地址,不能打印出上述格式化的内容，必须调用__repr__代替__str__

    __repr__ = __str__


def addStudent():
    studentName = threadLocal.studentName
    print('当前线程是%1s,该线程是用的变量student值是%2s' % (threading.current_thread().name, studentName))


def addStudentThread(name):
    threadLocal.studentName = name
    addStudent()


print('----------使用了threadlocal-------------')

thread1 = threading.Thread(target=addStudentThread, args=('Jack',))
thread2 = threading.Thread(target=addStudentThread, args=('Tom',))

thread1.start()
thread2.start()
thread2.join()
thread1.join()

print('----------使用了dict-------------------')

global_dict = {}


def addStd(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    task1()


def task1():
    print('当前线程是%1s,该线程使用的变量是%2s' % (threading.current_thread().name
                                     , global_dict[threading.current_thread()].__repr__))


dicThread1 = threading.Thread(target=addStd, args=('dictTom',))
dicThread2 = threading.Thread(target=addStd, args=('dictJack',))
dicThread1.start()
dicThread2.start()
dicThread1.join()
dicThread2.join()
