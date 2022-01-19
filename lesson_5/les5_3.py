"""
3. Создать текстовый файл (не программно), построчно записать фамилии
    сотрудников и величину их окладов. Определить, кто из сотрудников имеет
    оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
    средней величины дохода сотрудников.
"""
with open("3.txt", "r", encoding="UTF-8") as file_3:
    workers = []
    salary = 0
    count = 1
    for line in file_3:
        workers.append(line.split())
    for el in workers:
        if int(el[2]) < 20000:       # Поиск людей с зп ниже 20к
            print(' '.join(el))
            salary += int(el[2])     # ссумирование зп всех сотрудников
            count += 1               # кол-во сотрудников
    average_salary = salary / count  # средняя зп
    print(average_salary)
