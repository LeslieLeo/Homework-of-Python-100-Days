# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:07:33 2019
1英寸=2.54厘米。

@author: 刘立
"""

while True:
    a = float(input('输入想换算的数量：'))
    if a < 0:
        print('怎么会有负的长度啊摔！不干了！！(╯‵□′)╯︵┻━┻')
        break
    b = int(input('输入想换算的单位代号（0表示英寸，1表示厘米）：'))
    if b == 0:
        print('%.2f英寸 = %.2f厘米' % (a, a * 2.54))
    elif b == 1:
        print('%.2f厘米 = %.2f英寸' % (a, a / 2.54))
    else:
        print('输入其他的我咋知道你要换啥啊摔！(╯‵□′)╯︵┻━┻')
        
#标准答案
        
"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: 骆昊
"""

'''
value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')
'''