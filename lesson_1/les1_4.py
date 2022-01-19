"""
4. Пользователь вводит целое положительное число.
    Найдите самую большую цифру в числе.
    Для решения используйте цикл while и арифметические операции.
"""
number = 0
user_number = input('Введите целое положительное число\n>>> ')

if user_number.isdigit() and int(user_number) > 0:
    number = int(user_number)
else:
    print('Неверный ввод\nВведите целое положительное число')
    exit()

max_number = 0
while number != 0:
    current_number = number % 10
    number //= 10
    if max_number < current_number:
        max_number = current_number
print(f'Самая большая цифра в числе {user_number} это {max_number}')
