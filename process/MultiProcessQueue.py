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

'多进程实现平方计算'
__author__ = 'click'
__date__ = '2018/7/31 下午3:20'

from multiprocessing import Process, Queue
import random, time


# master
def master(queue):
    for i in range(10):
        n = random.randint(0, 10)
        print('往master队列中添加任务 %s' % n)
        queue.put(n)


# worker

def worker(queue):
    for i in range(10):
        try:
            n = queue.get(timeout=1)
            print('worker进程获取到master队列中的元素%s' % n)
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            print("worker进程输出计算结果%s" % r)
        except queue.Empty:
            print('队列为空')


if __name__ == '__main__':
    queue = Queue()

    masterProcess = Process(target=master, args=(queue,))
    workerProcess = Process(target=worker, args=(queue,))

    masterProcess.start()
    workerProcess.start()
    masterProcess.join()
    masterProcess.terminate()
