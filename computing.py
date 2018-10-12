# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:43:43 2017
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder 3.2.6
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：computing.py
"""

import time
import datetime
import functools  # 装饰器上装饰


# 定义计算函数运行时间
def timeIt(func):
    @functools.wraps(func)  # 装饰器上装饰后，运行函数时就直接返回运行函数
    def wrap(*arg, **kwargs):  # 定义多变量参数
        start = datetime.datetime.now()  # 定义函数运行开始时间，现在时间
        func(*arg, **kwargs)  # 运行函数
        end = datetime.datetime.now()  # 定义函数运行结束时间，现在时间
        cost = end-start
        print('%s , %s' % (func.__name__, cost))  # 运行的函数名称，运行的时间
    return wrap  # 调用函数本身不能加（），如果加（）则调用函数返回的值


@timeIt  # 装饰器，用于执行这个函数时，改变为执行装饰器函数
# 定义测试的函数
def func2(arg):
    time.sleep(arg)  # 等待时间


@timeIt
def func3(m, n):
    print('m + n = {0}'.format(m+n))


func2(2)
func3(1, 2)
