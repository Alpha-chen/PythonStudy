# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'@property属性使用'
__author___ = "click"


class Property(object):

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            print("高度必须大于0")
        else:
            print("输入高度合格")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            print("宽度必须大于0")
        else:
            print("设置的宽度合格")
        self.__width = value

    @property
    def resolution(self):
        return self.__width * self.__height

    def test(self):
        return self.resolution


if __name__ == '__main__':
    property = Property()
    property.height = 100
    property.width = 80
print(property.resolution)
