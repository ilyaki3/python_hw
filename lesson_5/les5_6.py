"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
    описывает учебный предмет и наличие лекционных, практических и лабораторных
    занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
    не обязательно были все типы занятий. Сформировать словарь, содержащий название
    предмета и общее количество занятий по нему. Вывести словарь на экран.

    Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —

    Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def to_zero(variable):
    if variable == '':
        variable = '0'
    return variable


def cleaning(hours):
    hours = hours.strip('(л)').strip('—').strip('.').strip('(пр)').strip('(лаб)')
    return hours


with open('6.txt', 'r', encoding='UTF-8') as f6:
    subj = {}
    for line in f6:
        subjects, lecture, practice, lab = line.split()

        lecture = int(to_zero(cleaning(lecture)))
        practice = int(to_zero(cleaning(practice)))
        lab = int(to_zero(cleaning(lab)))

        subj[subjects] = lecture + practice + lab
    print(subj)

