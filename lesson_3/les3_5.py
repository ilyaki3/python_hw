"""
5. Программа запрашивает у пользователя строку чисел,
разделенных пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо
числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале
нужно добавить сумму этих чисел к полученной ранее сумме и после
этого завершить программу.
"""

SYMBOLS = {'(', '+', ':', '$', '/', '_', '%', '~', '?', '"', '-',
           '`', '#', '*', '&', '!', '=', '.', ';', '^', ')', ',', '@'}
numbers_sum = 0
ex = True

while ex:
    user_input = input('Введите числа через пробел (спецсимвол для выхода):\n>>> ')
    numbers = user_input.split()
    i = 0
    while i < len(numbers):
        if numbers[i] in SYMBOLS:
            ex = False
            break
        numbers_sum += int(numbers[i])
        i += 1
    print(numbers_sum)
