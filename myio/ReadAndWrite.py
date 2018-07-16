#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'文件的读写操作'
__author__ = 'click'
__date__ = '2018/7/16 下午2:57'

readPath = r'/Users/xupangen/npm-debug.log'

with open(readPath, 'r') as f:
    s1 = f.read(1024)
    print(s1)
    print("---------------------")

    for f in f.readline():
        print(f.strip("\n"))


def readTxt():
    #open 不要放在try内部
    f = open(readPath, 'r')
    try:
        s = f.read()
        return s
    except IOError as e:
        print(e.args.__str__())
        return ""
    finally:
        f.close()


writePath = '/Users/xupangen/pythonIO.txt'

# "w":重新覆盖
# 'a':追加
with open(writePath, 'w') as f:
    # f.write(readTxt())
    f.write(readTxt())
