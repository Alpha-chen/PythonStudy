#!/usr/bin/env python
# -*- coding:utf-8 -*-

# name = input("输入你的名字:")
name ='小明'
a = input("请输入上一个学期的成绩:")
b = input("请输入这一个学期的成绩:")

c = a -b

if c>0:
    print('%s同学成绩相比上学期退步了%f%%' %(name ,((c/a)*100)))
else:
    print("%s同学成绩相比上学期进步了%f%%" %(name,((b-a)/a)*100))