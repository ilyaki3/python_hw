"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
    запросите у пользователя несколько чисел и строк и сохраните
    в переменные, выведите на экран.
"""

variable1 = 1
variable2 = 2

print(variable1)
print(variable2)

user_name = input('Как вас зовут?\n>>> ')
user_age = input('Сколько вам лет?\n>>> ')

if user_age.isdigit() and int(user_age) != 0:
    user_age = int(user_age)
else:
    print('Ошибка ввода.\nВведите ненулевое число.')
    exit()

age_ending = ''
if user_age % 10 == 1 and user_age != 11:
    age_ending = 'год.'
elif 1 < user_age % 10 < 5:
    age_ending = 'года'
else:
    age_ending = 'лет'

print(f'Имя: {user_name}\nВозраст: {user_age} {age_ending}')
