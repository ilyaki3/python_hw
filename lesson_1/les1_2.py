"""
2. Пользователь вводит время в секундах. Переведите время в часы,
    минуты и секунды и выведите в формате чч:мм:сс.
    Используйте форматирование строк.
"""
import datetime
input_seconds = input('Время в секундах:\n>>> ')

if input_seconds.isdigit():
    input_seconds = int(input_seconds)
else:
    print('Введите числовое значение')
    exit()

hours = input_seconds // 3600
minutes = input_seconds % 3600 // 60
seconds = input_seconds % 3600 % 60

print(f'{hours}:{minutes}:{seconds}')
print(datetime.time(hours, minutes, seconds))
