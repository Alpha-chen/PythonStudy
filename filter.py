# !/usr/bin/env python
# -*- coding:utf-8 -*-

# filter过滤

def no_empty(s):
    return s and s.strip()


# no_empty 函数返回true 则输出输入的字符， false不返回输入的字符
r_no = filter(no_empty, ['A', '', 'B', None, 'C', '  '])

print(list(r_no))


# 使用filter 赛选素数
# 生成素数
def generate_shu():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选规则
def filter_rule(n):
    return lambda x: x % n == 0;


# 取出数据,进行筛选
def filter_data():
    yield 2  # 表示先返回一个2 但函数还会继续执行下去

    it = generate_shu()

    while True:
        n = next(it)
        yield n
        it = filter(filter_rule, it)


# 测试
for n in filter_data():
    if n <= 1000:
        print(n)
    else:
        break