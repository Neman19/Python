# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 01:12:46 2021

@author: Ya
"""
n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break
