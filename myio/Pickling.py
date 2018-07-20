#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'序列化'
__author__ = 'click'
__date__ = '2018/7/20 下午3:37'

import pickle
import json

tesiDict = dict(name='bob', age='10')

# 序列化
print(pickle.dumps(tesiDict))
file = open('dump.txt', 'wb')
# 进行文件操作,将序列化的数据持久化到文件中
pickle.dump(tesiDict, file)
file.close()

# 读取文件序列化的数据

fileLoad = open('dump.txt', 'rb')
d = pickle.load(fileLoad)
fileLoad.close()
print(d)

# 转为JSON
jsonTest = dict(name='json', age='1000')
print("对象转为JSON")
# dump(obj,file)
jsonStr = json.dumps(jsonTest)
print(jsonStr)
print("json转对象")
# load(f)从文件中读取json字符串
jsonToObj = json.loads(jsonStr)
print(jsonToObj)


# 对象直接转为json
# 对象不能直接转为JSON 因为对象不是直接序列化,但是可以使用对象的__dict__方法

class ObjToJson(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


obj = ObjToJson('objToJson', '88888')
s = json.dumps(obj, default=lambda a: a.__dict__)
print("ObjToJson")
print(s)


def dictToObj(d):
    return ObjToJson(d['_ObjToJson__name'], d['_ObjToJson__age'])


s = json.loads(s)

print(dictToObj(s))

obj = dict(name='小明', age='20')
s = json.dumps(obj, ensure_ascii=True)
print('ensure_ascii')
print(s)
