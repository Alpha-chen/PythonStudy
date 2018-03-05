#!/usr/bin/rnv python
# -*- coding:UTF-8 -*-

a = input("请输入你的体重:")
weight = int(a)

b = input("请输入你的身高:")
height = int(b)

c = a / (b * b)

if c < 18.5:
    print("你的体重太轻了")
elif 18.5 < c < 25:
    print("你的体重正常")
elif 25 < c < 28:
    print("你的体重过重")
elif 28 < c < 32:
    print("你的体重肥胖")
elif c > 32:
    print("你的体重严重肥胖")
