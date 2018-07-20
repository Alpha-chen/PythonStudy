#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'获取文件及子文件中的文件名'
__author__ = 'click'
__date__ = '2018/7/17 下午2:33'

import os

'1.先获取到传入的路径'
'2.循环得到每一个文件/目录，并拼接为绝对路径'
'3.获取路径下的所有文件/目录'
'4.判断每一个 条目是文件,还是目录'
'5.目录重新循环步骤2'
'6.是文件则输出'

def getFilePaths(path='.'):
    print("getFilePaths->path=" + path + "\n")

    for x in os.listdir(path):
        abspath = os.path.join(path, x)
        if os.path.isdir(abspath):
            getFilePaths(abspath)
        else:
            yield abspath


path = input("请输入你要查找的目录:")


print('所有文件', [x for x in getFilePaths(path=path)])
