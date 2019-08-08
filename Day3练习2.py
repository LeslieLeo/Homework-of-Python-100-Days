# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:30:06 2019

我还是决定写一个丧心病狂的情趣骰子(╯‵□′)╯︵┻━┻

@author: 刘立
"""

#1.random.random()

#用于生成一个0到1的随机浮点数：0<= n < 1.0

#2.random.uniform(a,b) 

#用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
#如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。




import random

while True:
    start = int(input('开始请扣1：'))
    if start != 1:
        print('你叉叉，叫你抠1你不抠(╯‵□′)╯︵┻━┻')
        break
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = str()
    d = str()
    
    if a == 1:
        c = '舔'
    elif a == 2:
        c = '咬'
    elif a == 3:
        c = '吸'
    elif a == 4:
        c = '吹'
    elif a == 5:
        c = '揉'
    else:
        c = '捏'
        
    if b == 1:
        d = '双耳'
    elif b == 2:
        d = '娇唇'
    elif b == 3:
        d = '咪咪'
    elif b == 4:
        d = '肚脐'
    elif b == 5:
        d = '屁屁'
    else:
        d = '大腿'
        
    print(c,d)
    
#标准答案
"""
掷骰子决定做什么事情

Version: 0.1
Author: 骆昊
"""
'''
from random import randint

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)
'''