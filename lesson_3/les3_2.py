"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""


def data(name: str, surname: str, years: int, city: str, e_mail: str, telephone: str):
    print(name, surname, years, city, e_mail, telephone)


data(name='Илья', surname='Киреев', years=25, city='Москва',
     e_mail='aliwe2@yandex.ru', telephone='8-800-555-35-35')
