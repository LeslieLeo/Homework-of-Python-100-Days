# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:14:12 2019

@author: 刘立
"""
import math

while True:
    a = float(input('请在此输入第一条边的长度：'))
    b = float(input('请在此输入第二条边的长度：'))
    c = float(input('请在此输入第三条边的长度：'))
    if a + b <= c or a + c <= b or b + c <= a:
        print('这三条边不能组成三角形，请重新输入')
    else:
        C = a + b + c
        p = C / 2
        V = math.sqrt(p * (p - a) * (p - b) * (p - c))        
        print(('三角形的周长 = %.2f') % C)
        print(('三角形的面积 = %.2f') % V)
        break

#标准答案
"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
"""
'''
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % (area))
else:
    print('不能构成三角形')
'''