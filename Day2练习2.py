# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:28:33 2019
输入半径计算圆的周长和面积

@author: 刘立
"""
import math

r = float(input('请在此输入圆的半径：'))
pai = math.pi

C = 2*pai*r
V = pai*(r**2)

print('圆的周长为%s，面积为%s' % (C, V))







#答案
"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""

'''
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
'''

