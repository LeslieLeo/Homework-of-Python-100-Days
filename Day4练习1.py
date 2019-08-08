# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:12:00 2019

@author: 刘立
"""
number = int(input('请输入要判断的数：'))

for i in range(1, number + 1):
    if i != 1 and i != number and number % i == 0:
        print('%d不是质数' % number)
        break
    elif i == number and i != 1:
        print('%d是质数' % number)
    elif number == 1:
        print('%d不是质数' % number)
        break
        
#标准答案
"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
'''
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
'''
#如果一个数不是素数是合数， 那么一定可以由两个自然数相乘得到， 
#其中一个大于或等于它的平方根，一个小于或等于它的平方根，并且成对出现。