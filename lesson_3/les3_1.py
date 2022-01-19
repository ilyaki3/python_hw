"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def degree(a: str, b: str):
    """Деление первого числа на второе
    :param a: str Делимое
    :param b: str Делитель
    :return:
    """
    try:
        a = int(a)
        b = int(b)
        result = a / b
    except ValueError:
        return 'Ошибка. Введите число'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    return result


num_1 = input('Первое число:\n>>> ')
num_2 = input('Второе число:\n>>> ')

print(degree(num_1, num_2))
