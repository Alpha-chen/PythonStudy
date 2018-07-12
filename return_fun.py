#!/usr/bin/env python
# -*- coding:utf-8 -*-
def createCounter():
    n = 0
    def counter():
        nonlocal n
        n+=1
        return n
    return counter

count = createCounter()

print(count(),count(),count(),count())

print(createCounter.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper