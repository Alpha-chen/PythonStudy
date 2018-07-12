# !/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import reduce


# map
def fn(x, y):
    return x * 10 + y


arrays = reduce(fn, [1, 3, 5, 7, 9])


# print(list(arrays))


def is_old(x):
    return x % 2 == 1;


r = filter(is_old, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("is_old", list(r))



