'''
Курс: Основы языка Python
Урок 7. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
1)	Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
--------------------------------------------------------------------
31	22      **      3	5	32      **      3	5	8	3
37	43      **      2	4	6       **      8	3	7	1
51	86      **      -1	64	-8      **
--------------------------------------------------------------------
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка:
сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
====================================================================
'''

# importing standard modules
from random import randint
from copy import deepcopy
import numpy as np

# MATRIX class
class Matrix:
    def __init__(self, matrix=[], row=3, col=3):
        if matrix == []:                        # if the list with the matrix was not passed
            self.generate_matrix(row, col)      #  we will create it ourselves
        else:
            self.matrix = deepcopy(matrix)      # copy to the matrix attribute

    def generate_matrix(self, row, col, low_range=-1000, hi_range = 1000):
        self.matrix = []
        for x in range(row):
            self.matrix.append([])
            for y in range(col):
                self.matrix[x].append(randint(low_range, hi_range))

    def __str__(self):                          # to work as 'str' or 'print'
        len_field = 10                          # len cells for the matrix
        str_separate = '-' * (len(self.matrix[0]) * (len_field + 1) + 1) + '\n'     # separate line for good view
        out_str = str_separate
        for x in range(len(self.matrix)):
            out_str += '|'
            for y in range(len(self.matrix[x])):
                out_str += (str(self.matrix[x][y]).center(len_field)) + '|'
            out_str += '\n' + str_separate
        return out_str

    def __getitem__(self, item):        # to work as a list
        return self.matrix[item]

    def __iadd__(self, other):          # it can add both with the matrix and with the MATRIX class
        self.matrix = self.__sum_matrix(other)
        return self

    def __add__(self, other):           # it can add both with the matrix and with the MATRIX class
        return Matrix(self.__sum_matrix(other))

    def __sum_matrix(self, other):      # private method for summing two matrices (self + any_matrix)
        sum_matrix = []
        try:
            for x in range(len(self.matrix)):
                sum_matrix.append([])
                for y in range(len(self.matrix[0])):
                    sum_matrix[x].append(self.matrix[x][y] + other[x][y])
        except:
            print('Ошибочные параметры для операции (матрицы не эквивалентны)!!!')
        return sum_matrix


# the code block of the program
my_class = Matrix()         # creating an instance of a class with default parameters (matrix 3 row, 3 col)
print('перегрузка метода __str__() - печать матрицы:\n(класс сгенерил матрицу "по умолчанию" 3х3 - без параметров)')
print(my_class)             # printing a matrix using __str__

print('перегрузка метода __str__() - печать матрицы:\n(класс сгенерил матрицу c входными параметрами 10х8)')
my_class = Matrix([],10,8)  # create an instance of the class (matrix 10 row, 8 col)
print(my_class)             # printing a matrix using __str__

print('перегрузка метода __str__() - печать матрицы:\n(класс получил список с произвольной матрицей при инициации)')
my_list = [[-799, 728, 168, 907], [215, 679, -378, 87], [795, -515, 35, 544]]
my_class = Matrix(my_list)  # create an instance of the class with passing the matrix
print(my_class)             # printing a matrix using __str__

matrix_1 = Matrix([],3, 4)
matrix_2 = Matrix([],3, 4)

print('перегрузка метода __add__:\n(сгенерим две матрицы)')
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print('Сумма мартиц нашим методом:\n', matrix_3)
matrix_sum = np.matrix(matrix_1.matrix) + np.matrix(matrix_2.matrix)
print('Проверка через библиотеку NumPy:\n', matrix_sum)
print('перегрузка метода __iadd__:')
matrix_1 += matrix_2            # increase by matrix class
# matrix_1 += matrix_2.matrix     # increase by matrix
# matrix_1 += my_list             # increase by List (matrix)
print('Увеличение текущей матрицы:\n', matrix_1)

