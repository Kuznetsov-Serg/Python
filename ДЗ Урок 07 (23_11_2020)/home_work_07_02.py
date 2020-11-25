'''
Курс: Основы языка Python
Урок 7. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
====================================================================
'''

# importing standard modules
from abc import ABC, abstractmethod     #, abstractproperty

# Class definition block
class ClothesAbsClass(ABC):     # abstract class
    @property
    @abstractmethod             # decorator (@abstractmethod + @property = @abstractproperty)
    def name(self):             # this property will be supplied by the inheriting classes individually
        pass
    @property
    @abstractmethod             # decorator
    def amount_canvas(self):    # required method amount of fabric (canvas)
        pass

class Clothes(ClothesAbsClass):
    def __init__(self, type, name):
        self.type = type
        self.__name = name
    @property
    def name(self):
        return self.__name
    @property
    def amount_canvas(self):
        pass
    def __str__(self):
        out_str = 'Тип: ' + self.type + '\nНаименование: ' + self.name + '\nКоличество ткани: ' + str(self.amount_canvas)
        return out_str

class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(type=self.__class__.__name__, name=name)   # initializing the parent class with children parameters
        self.size = size
    @property
    def amount_canvas(self):
        return round((self.size / 6.5 + 0.5), 2)

class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(type='Костюм', name=name)                  # initializing the parent class with children parameters
        self.height = height
    @property
    def amount_canvas(self):
        return round((self.height * 2 + 0.3), 2)
    def __str__(self):
        out_str = 'Тип: ' + self.type + '\nНаименование: ' + self.name + '\nРостовка: ' + str(self.height) + '\nКоличество ткани: ' + str(self.amount_canvas)
        return out_str

# the code block of the program
# initiate instances of classes
my_coat = Coat('Пальто мужское укороченное', 7)
my_suit = Suit('Костюм мужской однобортный', 10)

# demonstration of the results
print(my_coat)
print(my_suit)
# print(my_coat.name)
# print(my_coat.amount_canvas)
# print(my_suit.name)
# print(my_suit.amount_canvas)
