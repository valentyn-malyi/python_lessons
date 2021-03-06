"""
Все последовательности обязаны поддерживаеть получение элементов по целочисленному
индексу. Многие последовательности также поддерживают получение срезов.

Поддержку обоих операций обеспечивает метод __getitem__(self, key).
Срезы представляются при помощи объектов класса slice. Вызов sequence[start:stop:step]
равносилен вызову sequence[slice(start, stop, step)], где пропуску соответствуещего
параметра среза соответствует None.
"""

my_list = [1, 4, 5, 7, 9]
print(my_list[4])
print(my_list[:3])

print()

print('Lorem ipsum dolor sit amet.'[10:-10])
print('Python'[0])

print()

print(range(10)[5:7])
print(range(3)[-1])
