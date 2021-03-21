# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:28:23 2021

@author: Ya
"""

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')
