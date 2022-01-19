"""
1. Создать программно файл в текстовом формате, записать
    в него построчно данные, вводимые пользователем. Об окончании
    ввода данных свидетельствует пустая строка.
"""


with open("1.txt", 'w', encoding='UTF-8') as file1:
    while True:
        user_input = input('Введите строку: ')
        if user_input == '':
            break
        print(user_input, file=file1)

