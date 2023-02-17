"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).
Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!
Process finished with exit code 0
Пример:
Введите первое число: 10
Введите второе число: 10
1.0
Process finished with exit code 0
"""


def mydiv(d1, d2):
    try:
        result = d1 / d2
    except ZeroDivisionError:
        result = 'Вы что? Пытаетесь делить на 0!'
    return result


number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

print(mydiv(number1, number2))
