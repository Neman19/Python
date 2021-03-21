# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:13:59 2021

@author: Ya
"""

products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз!')
            continue

        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть целым числом. Попробуйте еще раз!')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз!')
            continue

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз!')
        continue

    unit = tmp

    products.append((
        order,
        {
            'название': title,
            'стоимость': price,
            'количество': amount,
            'единицы измерения': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Формирование списка завершено? (Y/N)) ')
    if q.lower() == 'y':
        break
    if q.lower() == 'Y':
        break
    
analitics = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    analitics['title'].append(item['title'])
    analitics['price'].append(item['price'])
    analitics['amount'].append(item['amount'])
    analitics['unit'].add(item['unit'])

print(analitics)
