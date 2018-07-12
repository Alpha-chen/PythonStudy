# !/usr/bin/env python
# -*- coding:utf-8 -*-
import time, functools


#
#
# def metric(fn):
#     print('%s executed in %s ms' % (fn.__name__, 10.24))
#     return fn
#
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
#
#
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         t1 = time.time()
#         fn(*args, *kw)
#         t2 = time.time()
#         difTime = (t2 - t1)
#         1000
#         print('%s 执行 in %.4f ms' % (fn.__name__, difTime))
#         return fn
#
#     return wrapper
#
#
# # 测试
#
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     print("fast")
#     return x + y;
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     print("slow")
#     return x * y * z;
#
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


# -------计算函数的执行时间------------


def calculateFunTime(fun):
    # @functools.wraps(fun)
    def wraps(*args, **kwargs):
        startTime = time.time()
        fun(*args, **kwargs)
        endTime = time.time()
        print("fun %s 执行了 %.4f s" % (fun.__name__, endTime - startTime))
        return fun

    return wraps


@calculateFunTime
def testFun(x, y):
    time.sleep(1)
    print("testFun")
    return x + y


@calculateFunTime
def testFun2(x, y, z):
    time.sleep(2)
    print("testFun2")
    return x * y * z


test1 = testFun(2, 3)

test2 = testFun2(2, 3, 4)

print(testFun.__name__)
print(testFun2.__name__)
# if test1 != 5:
#     print("test传入值不等于5")
# elif test2 != 24:
#     print("test2传入值的乘积不等于24")
