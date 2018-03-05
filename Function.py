# !/usr/bin/env python
# -*- coding:utf-8  -*-

# 计算圆的面积
# 导入pi
import math


def area_of_circle(i):
    area = math.pi * i * i
    print('圆的面积:%.2f' % area)


def main():
    list = [1, 2, 3, 4]
    for x in list:
        area_of_circle(x)


main()

print(abs(-12))
print(max(1, 2, 3, 100))

#数据类型的转换
print(int(10.11))
print(str(10.11))
print(float(10))
print(bool("False"))
# print(hex('false'))
print(hex(10002))
