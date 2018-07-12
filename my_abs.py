# !/usr/bin/env python
# -*- coding:utf-8 -*-


def my_abs(i):
    if i > 0:
        return i
    elif i < 0:
        return -i
    elif i == 0:
        ### pass 什么都不做
        pass


print(my_abs(-1))
print(my_abs(1))
