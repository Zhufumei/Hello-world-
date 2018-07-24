# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:02:09 2018

@author: Z
"""

f=open('内蒙古.txt',encoding='gbk').readlines()
ls=[]
data=[]
for line in f:
    ls.append(str(line.split(',')[0].split('(')[1]))
    print(ls)
    
    
for line1 in f:
    data.append(line1.split(',')[1].split(')')[0])
    print(data)
