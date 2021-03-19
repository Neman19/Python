# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:15:21 2021

@author: Ya
"""

def div(*args):

    try:
        arg1 = int(input("Пожалуйста, введите делимое: "))
        arg2 = int(input("Пожалуйста, введите делитель: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Попытка деления на ноль!"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Попытка деления на ноль!")
    '''

print(f'result  {div()}')
