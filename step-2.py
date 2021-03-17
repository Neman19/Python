# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:56:47 2021

@author: Ya
"""

time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

