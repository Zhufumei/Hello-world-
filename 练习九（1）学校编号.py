# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 22:57:14 2018

@author: Z
"""

ls=open('all_school.txt',encoding='utf-8').readlines()
print('学校编号为：\n')
for i in range(0,2300):
    print(ls[i].split('-jianjie-')[1].split('.')[0])
