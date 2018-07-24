# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:56:19 2018

@author: Z
"""

问题一：优化代码 用函数的方式修改练习四 输出每一天的天气（函数）
问题二：打印温度折线图，使用函数来优化（必须要有返回值）

知识点：一
求列表中的最大数、最小数、长度、排序、倒序、添加元素
ls=[1,2,9,-1,10,8]
max(ls)
min(ls)
len(ls)
a=sorted(ls)###默认是升序
ls.append(9.9)###追加
ls.remove(9.9)
b=reversed(ls)###列表倒置

知识点：二
函数的语法1：
def 函数名（）:
    指令集合

函数的语法2（有参数的函数）
def 函数名（a,b,c,e):
    指令集合（a)
    指令集合（b,c,e)

函数的语法3（函数的返回值）：
def 函数名（a,b,c,e):
    指令集合（a)
    指令集合（b,c,e)
    return xxx
例题1：
def calc():
    b=4
    print(b)
calc()
例题2：
def calc(a,b):
    '计算两个数之和 a是一个数字 b也是一个数字'
    print('a和b相加是：'+str(a+b))
calc(3,4)
例题3：
def calc(a,b,c):
    return a+b+c
calc(1,2,3)
print(calc(1,2,3))

######问题一：
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=lincang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
print('{}weather:'.format(input))
def weather(a,b):
    print('第'+str(a)+'天')
    print('今天的天气情况为：'+str(data['list'][b]['weather'][0]['main']))
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)



def chart(a):
    b=data['list'][a]['main']['temp']
    c=str('_')*int(b)
    return c
print('从第一天到第五天的温度折线图:')
print('1'+chart(2))
print('2'+chart(10))
print('3'+chart(18))
print('4'+chart(26))
print('5'+chart(34))

import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=lincang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
def rank(a):
    return data['list'][a]['main']['temp']
a1=rank(2)
a2=rank(10)
a3=rank(18)
a4=rank(26)
a5=rank(34)
b=[a1,a2,a3,a4,a5]
print('这五天温度排序为：')
print(sorted(b))