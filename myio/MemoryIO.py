#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'内存读写'
__author__ = 'click'
__date__ = '2018/7/16 下午4:49'

from io import StringIO, BytesIO

strIO = StringIO()
strIO.write("Hello")
strIO.write(" ")
strIO.write("Python")
print("StringIO->=" + strIO.getvalue())

strIOTest = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = strIOTest.readline()
    if s == '':
        break
    print(s)

# ByteIo
byteIO = BytesIO()
byteIO.write("你好".encode('utf-8'))
print(byteIO.getvalue())

byteIOTest = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd')

s1 = byteIOTest.read()
print(s1)
