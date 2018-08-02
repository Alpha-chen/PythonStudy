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

'时间模块'
__author__ = 'click'
__date__ = '2018/8/1 下午2:47'

from datetime import datetime, timedelta

now = datetime.now()
print('当前时间\n%s' % now)
# 坑  datetime不支持2018 08 01 格式  只支持2018 8 1
dt = datetime(2018, 8, 1, 12, 20)
print('输出指定时间\n%s' % dt)
dtTimeStamp = dt.timestamp()
print('将时间转换为时间戳\n%s' % (dtTimeStamp))
print('时间戳转换为当前时区时间\n%s' % datetime.fromtimestamp(dtTimeStamp))
print('时间戳转换为格林尼治UTC+0 时间\n%s' % datetime.utcfromtimestamp(dtTimeStamp))
print('字符串时间转时间对象\n%s' % (datetime.strptime('2018-8-1 12:20:00', '%Y-%m-%d %H:%M:%S')))
print('时间对象转字符串\n%s' % (dt.strftime('%a,%b %d %H:%M')))
print('----------日期加减----------')
print('日期相加\n%s' % (now + timedelta(days=1, hours=1)))
print('日期相减\n%s' % (now - timedelta(days=1, hours=1)))
