"""
5. Создать (программно) текстовый файл, записать в него программно
    набор чисел, разделенных пробелами. Программа должна подсчитывать
    сумму чисел в файле и выводить ее на экран.
"""

import random


with open('5.txt', 'w', encoding='UTF-8') as file_5:
    total = 0
    for i in range(11):
        x = random.randint(0, 100)
        file_5.write(str(x) + ' ')
        total += x
    file_5.write('\ntotal = ' + str(total))

