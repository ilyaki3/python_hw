"""
4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую
    построчно данные. При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
"""

translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять'
}

with open('4.txt', 'r', encoding='UTF-8') as file_4:
    with open('4_1.txt', 'w', encoding='UTF-8') as file_4_1:
        for line in file_4:
            search = ' '.join([translate.get(i, i) for i in line.split()])  # поиск слова по словарю и замена на русское
            file_4_1.write(search + '\n')                                   # запись в новый файл
