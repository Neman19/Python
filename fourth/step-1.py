# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:16:01 2021

@author: Ya
"""

def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в у.е. '))
        bonus = int(input('Премия в у.е. '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
sal()
