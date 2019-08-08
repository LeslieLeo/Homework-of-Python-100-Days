# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 12:01:38 2019

@author: 刘立
"""

while True:
    a = float(input('请在此输入你的考试分数：'))
    if a < 0 or a > 100:
        print('你谎报成绩，不和你玩惹╭(╯^╰)╮')
        break
    elif a < 60:
        print('你的成绩水平为E级，你能做的岂止如此')
    elif a < 70:
        print('你的成绩水平为D级，一看你就天天打游戏')
    elif a < 80:
        print('你的成绩水平为C级，勉强挤进了学渣队伍')
    elif a < 90:
        print('你的成绩水平为B级，勉强脱离了学渣队伍')
    else:
        print('大佬！请收下我的膝盖！！OTZ')
        
#标准答案

"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Version: 0.1
Author: 骆昊
"""
'''
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)
'''