#!/usr/bin/env python
# -*- coding:utf-8 -*-

# list数组的使用


classmate = ['jack', 'mack', 'miky']

# len(classmate)数组的长度
print(len(classmate))

print(classmate[0])
# 获取数组的中最后一个元素
print(classmate[len(classmate) - 1])
# 直接使用-1为下标访问最后一个元素，-2，-3访问倒数第二个，第三个
print(classmate[-1])

# 数组中增删改查
# 追加
classmate.append("love")
print('list的追加:', classmate)
# 插入到特定的位置中
classmate.insert(1, "insert1")
print("list insert", classmate)
# 删除 pop
classmate.pop()
print(classmate)
# 删除指定的位置
classmate.pop(1)
print(classmate)

# 修改特定位置上的元素
classmate[1] = 'test'
print(classmate)

# 数组中元素数据类型可以不相同
classmate = ['test', 1, 1.2, True, None]
print(classmate)
classmate.append(['hhaha', 4, 5])
print(classmate)
print(len(classmate))
# 数组中存在数组，访问的时候按照多维数组的方式访问
print(classmate[5][0])

# Tuple 是一个不可变的数组，没有增加、删除、修改操作。其他的操作与list的操作相同
mates = (1, 2)
print(mates)
# 由于tuple的"()"定义与数学运算符中"()"相冲突，因此在定义集合中只有一个元素的tuple时,必须使用以下方式
# mates=(1,)
mates = (1,)
print(mates)

# 创建一个"伪可变"tuple
mates = (1, 2, ['3', 4, 5])
print(mates)
mates[2][0] = 3
print(mates)

mates[2].append(6)
print(mates)

# 本节练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple
print(L[0][0])
# 打印Python
print(L[1][1])
# 打印lisa
print(L[2][2])
