# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:54:35 2018

@author: Z
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:44:59 2018
练习题4：
1.打印每天18点的天气信息，温度，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文   application应用
3.打印温度折线图
    1----------
    2--------------------
    3-------
    4----------
4.获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
5.友情提示，根据温度提示穿衣，打伞，出门(可选)

全球5天天气
@author: Administrator
"""
#####问题一：打印每天18点的天气信息，温度，情况，气压，最高温度，最低温度:

import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=lincang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

print('7月17日的天气状况：')
print('温度:'+str(data['list'][2]['main']['temp']))
print('情况:'+str(data['list'][2]['weather'][0]['description']))
print('气压:'+str(data['list'][2]['main']['pressure']))
print('最高温度:'+str(data['list'][2]['main']['temp_max']))
print('最低温度:'+str(data['list'][2]['main']['temp_min']))

print('7月18日的天气状况：')
print('温度:'+str(data['list'][10]['main']['temp']))
print('情况:'+str(data['list'][10]['weather'][0]['description']))
print('气压:'+str(data['list'][10]['main']['pressure']))
print('最高温度:'+str(data['list'][10]['main']['temp_max']))
print('最低温度:'+str(data['list'][10]['main']['temp_min']))

print('7月19日的天气状况：')
print('温度:'+str(data['list'][18]['main']['temp']))
print('情况:'+str(data['list'][18]['weather'][0]['description']))
print('气压:'+str(data['list'][18]['main']['pressure']))
print('最高温度:'+str(data['list'][18]['main']['temp_max']))
print('最低温度:'+str(data['list'][18]['main']['temp_min']))

print('7月20日的天气状况：')
print('温度:'+str(data['list'][26]['main']['temp']))
print('情况:'+str(data['list'][26]['weather'][0]['description']))
print('气压:'+str(data['list'][26]['main']['pressure']))
print('最高温度:'+str(data['list'][26]['main']['temp_max']))
print('最低温度:'+str(data['list'][26]['main']['temp_min']))

print('7月21日的天气状况：')
print('温度:'+str(data['list'][34]['main']['temp']))
print('情况:'+str(data['list'][34]['weather'][0]['description']))
print('气压:'+str(data['list'][34]['main']['pressure']))
print('最高温度:'+str(data['list'][34]['main']['temp_max']))
print('最低温度:'+str(data['list'][34]['main']['temp_min']))



######问题二：写出英文版的天气-天气情况，用户输入英文   application应用:
input=input('please input city:')
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=lincang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
print('{}weather:'.format(input))
print('This weather in the first day:')
print('temperature:'+str(data['list'][2]['main']['temp']))
print('pressure:'+str(data['list'][2]['main']['pressure']))
print('description：'+str(data['list'][2]['weather'][0]['main']))
print('temp_min:'+str(data['list'][2]['main']['temp_min']))
print('temp_max:'+str(data['list'][2]['main']['temp_max']))

print('This weather in the second day:')
print('temperature:'+str(data['list'][10]['main']['temp']))
print('pressure:'+str(data['list'][10]['main']['pressure']))
print('description：'+str(data['list'][10]['weather'][0]['main']))
print('temp_min:'+str(data['list'][10]['main']['temp_min']))
print('temp_max:'+str(data['list'][10]['main']['temp_max']))

print('This weather in the third day:')
print('temperature:'+str(data['list'][18]['main']['temp']))
print('pressure:'+str(data['list'][18]['main']['pressure']))
print('description：'+str(data['list'][18]['weather'][0]['main']))
print('temp_min:'+str(data['list'][18]['main']['temp_min']))
print('temp_max:'+str(data['list'][18]['main']['temp_max']))

print('This weather in the forth day:')
print('temperature:'+str(data['list'][26]['main']['temp']))
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('description：'+str(data['list'][26]['weather'][0]['main']))
print('temp_min:'+str(data['list'][26]['main']['temp_min']))
print('temp_max:'+str(data['list'][26]['main']['temp_max']))

print('This weather in the fifth day:')
print('temperature:'+str(data['list'][34]['main']['temp']))
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('description：'+str(data['list'][34]['weather'][0]['main']))
print('temp_min:'+str(data['list'][34]['main']['temp_min']))
print('temp_max:'+str(data['list'][34]['main']['temp_max']))



######问题三：打印温度折线图:
data1=data['list'][2]['main']['temp']
data2=data['list'][10]['main']['temp']
data3=data['list'][18]['main']['temp']
data4=data['list'][26]['main']['temp']
data5=data['list'][34]['main']['temp']
num1=str('_')*int(data1)
num2=str('_')*int(data2)
num3=str('_')*int(data3)
num4=str('_')*int(data4)
num5=str('_')*int(data5)
print('这五天温度折线图:')
print('    1'+num1)
print('    2'+num2)
print('    3'+num3)
print('    4'+num4)
print('    5'+num5)


##############问题四：获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
a=data['list'][2]['main']['temp']
b=data['list'][10]['main']['temp']
c=data['list'][18]['main']['temp']
d=data['list'][26]['main']['temp']
e=data['list'][34]['main']['temp']
print('所有温度获取及排序如下:')
print(sorted([a,b,c,d,e]))
