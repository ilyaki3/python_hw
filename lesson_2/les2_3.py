"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']
seasons_dict = {
    1: 'Winter', 2: 'Winter', 12: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Autumn', 10: 'Autumn', 11: 'Autumn',
}

# Проверка ввода
while True:
    month = input('Введите номер месяца от 1 до 12\n>>> ')
    if month.isdigit() and 0 < int(month) < 13:
        month = int(month)
        break
    else:
        print('Ошибка ввода.')

# Получение месяца из словаря
print(seasons_dict.get(month))

# Получение месяца из списка
if 0 < month < 3 or month == 12:
    print(seasons_list[0])
elif 2 < month < 6:
    print(seasons_list[1])
elif 5 < month < 9:
    print(seasons_list[2])
elif 8 < month < 12:
    print(seasons_list[3])
