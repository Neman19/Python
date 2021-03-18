# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:28:45 2021

@author: Ya
"""
my_list = [12, None, -77, 'True', True, 9.5]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)

