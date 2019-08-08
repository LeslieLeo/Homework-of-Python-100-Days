# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:38:15 2019

@author: 刘立
"""
#求模：求两个整数相除之后的余数

while True:
    a = int(input('输入年份：'))
    if a == 0:
        break
    b = a % 4
    c = a % 100
    d = a % 400
    
    if c == 0:     
        if d == 0:         
            print('此年份是闰年')
        else:
            print('此年份不是闰年')
    else:
        if b == 0:
            print('此年份是闰年')
        else:
            print('此年份不是闰年')



'''
一开始自己写的错误答案
while True:
    a = int(input('输入年份：'))
    if a == 0:
        break
    b = a/4
    c = a/100
    d = a/400
    
    if type(c) == int:     
        if type(d) == int:
         
            print('此年份是闰年')
        else:
            print('此年份不是闰年')
    else:
        if type(b) == int:
            print('此年份是闰年')
        else:
            print('此年份不是闰年')
'''

#标准答案
'''
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
'''
