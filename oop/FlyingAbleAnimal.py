#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
''
__author__ = 'click'
__date__ = '2018/7/13 上午10:11'

import oop.Animal


class FlyingAbleAnimal(object, oop.Animal):

    def fly(self):
        print("我能飞")
