# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:57:40 2018

@author: Z
"""

#######问题一天气提醒：
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=ganzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
def weather(a,b):
    print('第'+str(a)+'天')
    print('今日温度：'+str(data['list'][b]['main']['temp']))
    print('今日天气情况:'+str(data['list'][b]['weather'][0]['description']))
    a=str(data['list'][b]['weather'][0]['main'])
    if a=='Clear':
        print('今日晴空万里，适合在家吃西瓜吹空调，如需出门请注意防晒降温~')
    elif a=='Rain':
        print('今日将有雨，如需出门记得带伞避雨~')
    elif a=='Clouds':
        print('今日也无风雨也无晴，适合外出与家人朋友聚会~')
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)

##############问题二：淘宝客户端
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&ajax=true').read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
def shoppingtips():
    for i in range(0,36):
        title=data['mods']['itemlist']['data']['auctions'][i]['title']
        view_sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
        print('商品名为：'+str(title))
        print('商品销量为:'+str(view_sales))
        print('商品价格为：'+str(price))
        a=float(str(data['mods']['itemlist']['data']['auctions'][i]['view_price']))
        if a<=100.00:
            print('此商品物美价廉')
        elif a<=200.00:
            print('此类商品价格适中，为大多数消费者的选择')
        elif a>200.00 and a<=400.00:
            print('此类商品价格偏贵，为少数人的选择')
        while a>400:
            break
shoppingtips()