# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:42:51 2021

@author: Ya
"""

var_list = []

while True:
    item = input('Пожалуйста, введите элемент списка: ')
    var_list.append(item)

    q = input('Формирование списка завершено? (Y/N)) ')
    if q.lower() == 'y':
        break
    if q.lower() == 'Y':
        break
    
last_idx = len(var_list) - 1

for idx, _ in enumerate(var_list):
    if idx % 2 == 0 and idx < last_idx:
        var_list[idx + 1], var_list[idx] = var_list[idx:idx + 2]

print(var_list)
