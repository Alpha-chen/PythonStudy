#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'枚举类'
__author__ = 'click'
__date__ = '2018/7/13 下午4:28'

from enum import unique, Enum


@unique
class GenderEnum(Enum):
    MALE = 0,
    FAMALE = 1


class Student(object):

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    @property
    def getGender(self):
        return self.__gender

    @property
    def getName(self):
        return self.__name

    def __str__(self):
        print("Student %s %s" % (self.__name, self.__gender))

    def __call__(self):
        print("Student %s %s" % (self.__name, self.__gender))


if __name__ == '__main__':
    s = Student('小明', GenderEnum.FAMALE)
    # print(s)
print(s.__str__())

if s.getGender == GenderEnum.FAMALE:
    print("学生 %s 性别是 %s" % (s.getName, GenderEnum.FAMALE))
elif s.getGender == GenderEnum.MALE:
    print("学生 %s 性别是 %s" % (s.getName, GenderEnum.MALE))
