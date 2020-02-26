﻿"""Операции над множествами, которые являются методами, принимают в качестве
аргументов любые итерабельные объекты. Операции над множествами, записанные
в виде бинарных операций, требуют, чтобы второй операнд операции тоже был
множеством, и возвращают множество того типа, которым было первое множество
"""

print(frozenset('abc').union(frozenset('cdef')))  # корректно
print(frozenset('abc') | frozenset('cdef'))  # корректно
print(frozenset('abc').union('cdef'))  # корректно
print(frozenset('abc') | 'cdef')  # ошибка
