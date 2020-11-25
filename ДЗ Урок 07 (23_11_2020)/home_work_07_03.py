'''
Курс: Основы языка Python
Урок 7. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
3)	Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение.
Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание.
Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение.
Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление.
Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
====================================================================
'''

# Class definition block
class OrganicCell:
    def __init__(self, amount_cell):
        self.amount_cell = amount_cell
    def __str__(self):
        return str(self.amount_cell)
    def __add__(self, other):
        if self.__is_class(other):                  # check for membership in the class
            return OrganicCell(self.amount_cell + other.amount_cell)
        return self
    def __sub__(self, other):
        if self.__is_class(other):                  # check for membership in the class
            result = self.amount_cell - other.amount_cell
            if result > 0:
                return OrganicCell(result)
            else:
                print('В исходной клетке недостаточно ячеек для вычитания!')
                return None
    def __mul__(self, other):
        if self.__is_class(other):                  # check for membership in the class
            return OrganicCell(self.amount_cell * other.amount_cell)
        return self
    def __truediv__(self, other):
        if self.__is_class(other):                  # check for membership in the class
            try:
                result = int(self.amount_cell / other.amount_cell)
                if result > 0:
                    return OrganicCell(result)
                else:
                    print('Клетка не может состоять менее, чем из 1-й ячейки!')
            except:
                print('Ошибка деления!!!')
        return None
    def __is_class(self, other):
        try:
            if other.__class__.__name__ == self.__class__.__name__:
                return True
        except:
            pass
        print('В качестве параметра операции ожидается класс', self.__class__.__name__)
        return False
    def make_order(self, amount_cell_in_row):
        i, j = divmod(self.amount_cell, amount_cell_in_row)
        return (('*' * amount_cell_in_row + '\n') * i + '*' * j)

# the code block of the program
# initiate instances of classes
my_class1 = OrganicCell(10)
my_class2 = OrganicCell(15)
print('При сложении класса ({}) с классом ({}), получим класс ({})\n'.format(my_class1, my_class2, my_class1 + my_class2))
print('При сложении класса ({}) с числом ({}), получим класс ({})\n'.format(my_class1, 20, my_class1 + 20))
# my_class3 = my_class1 - my_class2   # There are not enough cells in the source cell for subtraction
print('При вычитании из класса ({}) класса ({}), получим ({})\n'.format(my_class1, my_class2, my_class1 - my_class2))
print('При вычитании из класса ({}) класса ({}), получим класс ({})\n'.format(my_class2, my_class1, my_class2 - my_class1))
print('При умножении класса ({}) на класс ({}), получим класс ({})\n'.format(my_class1, my_class2, my_class1 * my_class2))
print('При делении класса ({}) на класс ({}), получим ({})\n'.format(my_class1, my_class2, my_class1 / my_class2))
print('При делении класса ({}) на класс ({}), получим класс ({})\n'.format(my_class2, my_class1, my_class2 / my_class1))

print('Для класса ({}) метод "make_order" с параметром ({}) дает результат:\n{}'.format(my_class1, 4, my_class1.make_order(4)))
print('Для класса ({}) метод "make_order" с параметром ({}) дает результат:\n{}'.format(my_class2, 5, my_class2.make_order(5)))

