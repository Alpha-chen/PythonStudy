#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'python程序的几种调试方法'
__author__ = 'click'
__date__ = '2018/7/16 下午1:39'

import logging

logging.basicConfig(level=logging.INFO)


# print  大法好

# 断言

def assertTest(i):
    assert i != 0, "i 不等于0"
    n = 10 / i
    print("assertTest->=" + str(n))


def loggingTest():
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)


print(assertTest(1))
print(loggingTest())
