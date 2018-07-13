#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
''
__author__ = 'click'
__date__ = '2018/7/13 上午9:55'


class AnimalMixlnExtends(object):

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return "AnimalMixlnExtends->__name=" + self.__name

    __repr__ = __str__


if __name__ == '__main__':
    animal = AnimalMixlnExtends("猴子")
    print(animal.__repr__())
