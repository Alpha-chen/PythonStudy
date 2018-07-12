# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'面向对象编程实例'

__author__ = "click"

import sys


class Flower(object):

    # 变量前加上"__"表示该变量为私有变量,外部函数不能修改该变量的值
    def __init__(self, color, name):
        self.__color = color
        self.__name = name

    def printFlower(self):
        print("Flower属性分别为 %s %s" % (self.__color, self.__name))

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color;

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


if __name__ == '__main__':
    flower = Flower("绿色", "绿萝")
    # 以下代码无效
    flower.__name = "hua"
    print("flower.__name->=" + flower.__name)
    # 为什么flower.name 打印为"化",而printFlower方法确实"绿萝"呢？ 因为python解析器已经将对象的__name解释为_Student__name
    # 使用get set方法
    # flower.setName("花花")
    flower.height = 10
    flower.age = 2

    flower.printFlower()

    print(hasattr(flower, "__name"))
    print(getattr(flower, "__name"))
