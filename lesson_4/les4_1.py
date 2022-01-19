"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать
формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

try:
    hours = int(argv[1])
    pay = int(argv[2])
    bonus = int(argv[3])
    salary = hours * pay + bonus
    print(salary)
except ValueError:
    print('Ошибка ввода')
