# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:49:42 2019

@author: 刘立
"""

a = int(input('请输入要判断的第一个正整数：'))
b = int(input('请输入要判断的第二个正整数：'))


for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print('%d和%d的最大公约数为%d' % (a, b, i))
        break
for j in range(max(a,b), a * b + 1):
    if j % a == 0 and j % b == 0:
        print('%d和%d的最小公倍数为%d' % (a, b, j))
        break