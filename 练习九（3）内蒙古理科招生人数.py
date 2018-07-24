# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:05:34 2018
请求的URL
http://www.gaokaopai.com/university-ajaxGetMajor.html
求情的数据
id=3319&type=2&city=34&state=1
学校编号   理科2        城市        正常

作业10：
1.获取2300所学校的编号
2.获取31所城市的编号
3.获取142600数据，31/30,每个组有三个城市数据，后面组装在一起
4.将142600数据使用spark统计
@author: Administrator
"""
####获取2300所学校
ls=open('all_school.txt',encoding='utf-8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
 

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}

f=open('全国内蒙古理科人数.txt','a',encoding='utf-8')
Afor schoolid in schoolls[0:2300]:
        req=r.Request(url,data='id={}&type=2&city=50&state=1'.format(schoolid).encode(),headers=headers)
        f.write(r.urlopen(req).read().decode('utf-8','ignore')+"\n")
f.close()
        












