# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:57:07 2018

@author: Z
"""

##################问题一：
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&ajax=true').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def items(a):
    print('第'+str(a+1)+'个商品信息为：')
    title=data['mods']['itemlist']['data']['auctions'][a]['title']
    price=data['mods']['itemlist']['data']['auctions'][a]['view_price']
    view_fee=data['mods']['itemlist']['data']['auctions'][a]['view_fee']
    item_loc=data['mods']['itemlist']['data']['auctions'][a]['item_loc']
    view_sales=data['mods']['itemlist']['data']['auctions'][a]['view_sales']
    print('商品名为：'+str(title))
    print('商品价格为：'+str(price))    
    print('商品邮费为:'+str(view_fee))
    print('发货地址为:'+str(item_loc))
    print('商品销量为:'+str(view_sales))
def items_shop(b):
    items(b)
    items(b+1)
    items(b+2)
    items(b+3)
    print('*'*50)
items_shop(0)
items_shop(4)
items_shop(8)
items_shop(12)
items_shop(16)
items_shop(20)
items_shop(24)
items_shop(28)
items_shop(32)


################问题二：
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&ajax=true').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def items(a):
    print('第'+str(a+1)+'个商品信息为：')
    title=data['mods']['itemlist']['data']['auctions'][a]['title']
    price=data['mods']['itemlist']['data']['auctions'][a]['view_price']
    view_fee=data['mods']['itemlist']['data']['auctions'][a]['view_fee']
    item_loc=data['mods']['itemlist']['data']['auctions'][a]['item_loc']
    view_sales=data['mods']['itemlist']['data']['auctions'][a]['view_sales']
    print('商品名为：'+str(title))
    print('商品价格为：'+str(price))    
    print('商品邮费为:'+str(view_fee))
    print('发货地址为:'+str(item_loc))
    print('商品销量为:'+str(view_sales))
def items_shop(b):
    items(b)
    items(b+1)
    items(b+2)
    items(b+3)
items_shop(0)
items_shop(4)
items_shop(8)
items_shop(12)
items_shop(16)
items_shop(20)
items_shop(24)
items_shop(28)
items_shop(32)

################问题三：
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&ajax=true').read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
def items():
    for x in range(0,36):
        title=data['mods']['itemlist']['data']['auctions'][x]['title']
        price=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        view_fee=data['mods']['itemlist']['data']['auctions'][x]['view_fee']
        item_loc=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        view_sales=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        print('商品名为：'+str(title))
        print('商品价格为：'+str(price))    
        print('商品邮费为:'+str(view_fee))
        print('发货地址为:'+str(item_loc))
        print('商品销量为:'+str(view_sales)) 
items()

ls=[]
def price():
    for x in range(0,36):
        price=float(data['mods']['itemlist']['data']['auctions'][x]['view_price'])
        ls.append(price)
    return ls
price()
a=sorted(ls)
b=list(reversed(a))
print('所有商品价格从高到低排序为：')
print(b)

##### 问题四：
ls1=[]
def sales():
    for x in range(0,36):
        sales=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        y=int(sales[0:-3])
        ls1.append(y)
    return ls1
sales()
a1=sorted(ls1)
print('所有商品按销量排序为：')
print(a1)


######问题五： 
def post_fee():
    for i in range(0,36):
        if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0.0:
            print('第'+str(i+1)+'件商品包邮')
post_fee()
c=post_fee()
print(c)