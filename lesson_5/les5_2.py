"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("2.txt", "r", encoding="UTF-8") as file_2:
    count_lines = 0
    for line in file_2:
        words = [line.split()]
        count_words = (len(words[0]))
        count_lines += 1
        print(f'Строка: {count_lines} Слов: {count_words}')
print(file_2.closed)
