# !/usr/bin/env python
# -*- coding:utf-8 -*-


# for 循环
# range(n,m):生一个组数字，从n->(n-1)的整数
# list将生成的整数转换为一个list

# list = list(range(0, 101))
list = tuple(range(0, 101))
# 0-100的和
sum = 0
for x in list:
    sum = sum + x

print(sum)

# while 循环


count = 100
while count > 0:
    sum = sum + count
    if count == 50:
        print(count)
        # continue 死循环

    count = count - 1

print("end->", sum)

# 循环打出list中的名字
L = ['Bart', 'Lisa', 'Adam']
for s in L:
    print("hello, %s" % s)
