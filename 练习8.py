# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:27:14 2018

@author: Z
"""
import urllib.request as r
f=open('发货地址为福建的裙子淘宝数据.txt','w',encoding='utf-8')
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E7%A6%8F%E5%BB%BA&s={}&ajax=true'
for i in range(0,100):
    url1=url.format(i*44)
    try:
        data=r.urlopen(url1).read().decode('utf-8','ignore')
        f.write(data+'\n')
        print('第{}行'.format(i+1))
    except Exception as err:
        print('此行有误')
f.close()



