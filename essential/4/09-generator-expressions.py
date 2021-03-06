"""
Некоторые простые генераторы могут быть записаны в виде выражения.
Они выглядят как выражение, содержащее некоторые переменные, после
которого одно или несколько ключевых слов for, задающих, какие значения
должны принимать данные переменные (синтаксис соответствует заголовку
    цикла for), и ноль или несколько условий, фильтрующих генерируемые
значения (синтаксис соответствует заголовку оператора if). Такие выражения
называются выражениями-генераторами (generator expressions).
"""

generator = (x ** 2 + y for x in range(2, 7) for y in range(3) if x != 6)
for number in generator:
    print(number)

print()

print(sum(2 * x for x in range(5)))
