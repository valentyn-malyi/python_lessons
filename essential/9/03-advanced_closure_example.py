﻿"""Демонстрация часто допускаемой ошибки и способа её решения"""

def make_powers(n):
    """Функция, возвращающая список функций, каждая из которых вычисляет
    степень аргумента, равную данному индексу плюс 1
    (неправильная реализация)
    """

    functions = []

    for i in range(1, n + 1):
        functions.append(lambda x: x ** i)

    return functions


for function in make_powers(3):
    print(function(2))

# Видно, что результататом было не 2, 4, 8, как можно было бы ожидать,
# а 8, 8, 8

print()

# Причиной этого является так называемое позднее связываение.  К тому моменту,
# когда вызываются функции из списка, цикл в функции make_powers уже выполнен и
# переменная i всегда равна n + 1.

# Для того, чтобы избавиться от этого, необходимо скопировать данную переменную
# в локальные переменные каждой функции.  Единственный способ создать локальную
# переменную в лямбда-выражении -- это создать параметр функции.

def make_powers(n):
    """Функция, возвращающая список функций, каждая из которых вычисляет
    степень аргумента, равную данному индексу плюс 1
    (правильная реализация)
    """

    functions = []

    for i in range(1, n + 1):
        functions.append(lambda x, i=i: x ** i)

    return functions


for function in make_powers(3):
    print(function(2))