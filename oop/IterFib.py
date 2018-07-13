#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'使用__iter__生成斐波那契数列'
__author__ = 'click'
__date__ = '2018/7/13 下午3:21'


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    # 使用__iter__ 方法生成迭代对象,此时的Fib对象 可以理解为一个list/tuple
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # 运算到10000
            raise StopAsyncIteration

        return self.a  # 返回一个值


for n in Fib():
    print(n)
