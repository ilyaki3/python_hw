"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

user_number = input('Введите число n\n>>> ')

if user_number.isdigit():
    user_number_n = int(user_number)
    user_number_nn = int(user_number * 2)
    user_number_nnn = int(user_number * 3)

    sum_nnn = user_number_n + user_number_nn + user_number_nnn

    print(f'Сумма чисел {user_number_n} + {user_number_nn} + {user_number_nnn} = {sum_nnn}')

else:
    print('Введите числовое значение')
    exit()
