# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:06:50 2021

@author: Ya
"""

while 1:
    i = input('Пожалуйста введите числа разделённые\n'
                     'пробелами (допускаются int, float): ')
    i = i.split(" ")
    a = 0
    while a<len(i):
        try:
            i[a] = int(i[a])
        except ValueError:
            print("Value Error")
            break
        a = a + 1
    z = 0
    for c in i:
        z = z + c
    print(z)
    


