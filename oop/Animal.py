#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'多重继承'
__author__ = 'click'
__date__ = '2018/7/13 上午9:59'

class Animal(object):

    def __init__(self,name):
        self.__name= name

    def name(self):
        print("我是"+self.__name)

