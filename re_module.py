# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 08:45:14 2021

@author: vijay kalimuthu
"""
import re

#segment1 - using search method

paragraph = "please all of you if you have any issue contact me in vijaykala15me168@gmail.com "
req_format = re.compile("[a-zA-Z0-9]+@+[a-zA-Z]+\.[a-zA-Z]+") #email format
output= req_format.search(paragraph)
print(output)  # output = vijaykala15me168@gmail.com


#segment2 - using findall method

para = "I love you so much d udaya"
condition = re.compile("[a-zA-Z0-9]+")
ans = condition.findall(para)
print(ans[0])  # ans = ['I', 'love', 'you', 'so', 'much', 'd', 'udaya']
