# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:48:44 2021

@author: Ya
"""

seasons_list = [
    ['Зима', ['12', '1', '2']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]

seasons_dict = {
    'Зима': ['12', '1', '2'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']
}

while True:
    month_number = input('Пожалуйста, введите номер месяца: ')
    if month_number not in sum(seasons_dict.values(), []):
        print('Неправильно введенный номер месяца. Попробуйте еще раз!')
        continue

    break

for season, months in seasons_list:
    if month_number in months:
        print(f'Через список определено, что месяц с номером {month_number} - это время года {season}')

for season, months in seasons_dict.items():
    if month_number in months:
        print(f'Через словарь определено, что месяц с номером {month_number} - это время года {season}')
