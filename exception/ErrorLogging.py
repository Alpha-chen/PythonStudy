#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'异常,报错,日志打印'
__author__ = 'click'
__date__ = '2018/7/13 下午6:06'
from functools import reduce


def getExceptionLogging():
    try:
        print("try")
        r = 10 / int('2')
        print("r->=" + r)
    except ValueError as e:
        print("except")
        print('ValueError-=' + e)
    finally:
        print("finnaly")


# print(getExceptionLogging())


def str2num(s):
    return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
