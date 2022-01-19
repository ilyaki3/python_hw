"""
3. Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""


def my_func(var_1: int, var_2: int, var_3: int):
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    elif var_1 >= var_2 and var_3 >= var_2:
        return var_1 + var_3
    else:
        return var_2 + var_3


print(my_func(10, 20, 30))
