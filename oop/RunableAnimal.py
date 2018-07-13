#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
''
__author__ = 'click'
__date__ = '2018/7/13 上午10:09'

import oop.Animal


class RunableAnimal(object, oop.Animal):


    def run(self):
        print("我可以跑")
