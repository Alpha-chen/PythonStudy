# !/usr/bin/env python
# -*- coding:utf-8 -*-
from operator import itemgetter

# 排序sorted算法
lsit = [-12, -2, -24, 20, 39, 10];
print(sorted(lsit))

# sorted 函数接受一个key作为参数,以这个key作为排序的规则
print(sorted(lsit, key=abs))

# 忽略大小写 排序字符

listStr = ["C", "s", "a", "A", "z", "O"];
# 使用所有的字符转为小写,然后根据ascii码相应字符的排序进行比较
print(sorted(listStr, key=str.lower))

print(sorted(listStr, key=str.lower, reverse=True))

# sort排序 数组中的字段

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

# operator.itemgetter 获取sortedlist中某一个下标下的数字
print(sorted(students, key=itemgetter(1)))
print(sorted(students, key=itemgetter(1,0)))

print(sorted(students, key=lambda x: students[1]))
