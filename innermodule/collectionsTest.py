#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

#
# _ooOoo_
# o8888888o
# 88" . "88
# (| -_- |)
#  O\ = /O
# ___/`---'\____
# .   ' \\| |// `.
# / \\||| : |||// \
# / _||||| -:- |||||- \
# | | \\\ - /// | |
# | \_| ''\---/'' | |
# \ .-\__ `-` ___/-. /
# ___`. .' /--.--\ `. . __
# ."" '< `.___\_<|>_/___.' >'"".
# | | : `- \`.;`\ _ /`;.`/ - ` : | |
# \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
# `=---='
# .............................................
#           佛曰：bug泛滥，我已瘫痪！
#

'常用的集合'
__author__ = 'click'
__date__ = '2018/8/2 下午4:37'

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple,用来自定义一个tuple,可以规定tuple的个数
# ,并且可以使用定义的属性代替索引进行取值

Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(1, 1, 4)
print('namedtuple横坐标(x)%1s 纵坐标(y)%2s 半径(r)%3s' % (circle.x, circle.y, circle.r))
# 提升 插入、删除效率的deque

q = deque(['1', 2, '3'])
print('deque%s' % q)
q.append('4')
print('deque追加%s' % q)
q.appendleft("0")
print('deque左边追加%s' % q)

print('deque删除%s' % q.pop())
print('deque删除头部%s' % q.popleft())
q.extend(['6', '7', '8'])
print('deque右边扩展一个队列%s' % q)
q.extendleft(['-1', '-2', '-3'])
print('deqiue左边扩展一个队列%s' % q)

# defaultDict 带有默认的dict，当访问的额key不存在时候,返回一个默认的值
defaultdicts = defaultdict(lambda: 'Key is not exits')
defaultdicts['name'] = 'tom'
print('defaultDict->name=%s' % defaultdicts['name'])
print('defaultDict->grade=%s' % defaultdicts['grade'])

# orderdict
od = OrderedDict([('a', 1), ('c', 2), ('b', 3)])
print('orderdict内容%s' % od)

# counter
counter = Counter()

for ch in 'Hello,Python':
    counter[ch] = counter[ch] + 1

print('字符串中各字符出现次数%s' % counter)
