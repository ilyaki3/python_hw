#pylint:disable=C0301
"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""
a = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


class Matrix:
    def __init__(self, data):
        self.data = data
        
    def __str__(self):
        return '\n'.join(['\t'.join([str(i) for i in el]) for el in a])
    
    def __add__(self, m2):
        for k in range(len(self.data)):
            for v in range(len(self.data[k])):
                self.data[k][v] += m2.data[k][v]
        return Matrix(self.data)
        
c = Matrix(a)
d = Matrix(b)       
e = c+d
print(e)
print(isinstance(e, Matrix))
