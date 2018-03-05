# !/usr/bin/env python
# -*- coding:utf-8 -*-


# 声明一个字典
classGrade = {'miky': 95, 'jack': 80, 'miky1': 100}

print(classGrade)

# 打印某一个key的值
print(classGrade['miky'])

# 更改一个key的value
classGrade['miky'] = 100
print(classGrade['miky'])

#删除一个特殊的元素
classGrade.pop('miky')
print(classGrade)
# 如果key值没有,使用get避免闪退。如果使用直接获取就会闪退
# print(classGrade['miky']) 不推荐
print(classGrade.get('miky'))

# print(classGrade['miky2'])
# 与list相比 dict 查询，插入的速度更快，不会随着key的增加而变慢，但是占用的内存也越大
# dict的key必须不可变，所以key不能使list


# set 是一个key值不能重复的集合,自动过滤重复的元素
setTest = set([1, 2, 3, 'ssss', 2])
print(setTest)
# set 中添加元素
setTest.add(20)
print(setTest)
# 删除元素
setTest.remove(20)
print(setTest)
list = ['i','w','e']
# set 内部的元素不能使可变数组，因为list不是一个可以做hash值的数据类型
# setTest.add(list)
# 不能做hash值得的类型不能作为唯一的key值
# tuple=('i','w','e',['1','2',3])
setTest.add(tuple)
print(setTest)
#set可以做 数学集合的计算 交集,并集
