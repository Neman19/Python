# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:37:53 2021

@author: Ya
"""

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
 
 
print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))

      
  

