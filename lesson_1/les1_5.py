"""
5. Запросите у пользователя значения выручки и издержек фирмы.
    Определите, с каким финансовым результатом работает фирма
    (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
    Выведите соответствующее сообщение. Если фирма отработала с прибылью,
    вычислите рентабельность выручки (соотношение прибыли к выручке).
    Далее запросите численность сотрудников фирмы и определите прибыль
    фирмы в расчете на одного сотрудника.
"""


def input_check(user_input):
    if user_input.isdigit():
        user_input = int(user_input)
        return user_input
    else:
        print('Ошибка. Введите числовое значение')
        exit()


revenue = input('Выручка фирмы\n>>> ')
costs = input('Издержки фирмы\n>>> ')

revenue = input_check(revenue)
costs = input_check(costs)

profit = 0
rentability = 0
if revenue > costs:
    profit = revenue - costs
    rentability = revenue / costs
    print(f'Фирма отработала с прибылью: {profit}\nРентабельность: {rentability:.1f}')
elif revenue < costs:
    profit = costs - revenue
    print(f'Фирма отработала с убытком в {profit}')
else:
    print('Фирма работает в 0')

workers_count = input('Введите колличество сотрудников\n>>> ')
workers_count = input_check(workers_count)

worker_profit = profit / workers_count
print(f'Прибыль фирмы в расчете на одного сотрудника равна: {worker_profit:.1f}')
