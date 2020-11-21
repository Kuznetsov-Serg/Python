'''
Курс: Основы языка Python
Урок 6. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
5)	Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
====================================================================
'''

# Class definition block
class Stationery:
    def __init__(self, name):
        self.title = name
    def draw(self):
        print('Зауск отрисовки')

class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')
    def draw(self):
        super().draw()
        print('В жизни легче дойти до ручки, чем до сути.')

class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')
    def draw(self):
        super().draw()
        print('Все ошибаются, даже на карандашах есть ластики.')

class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')
    def draw(self):
        super().draw()
        print('Имея один маркер, можно изрисовать всё, кроме этого маркера.\nИмея два маркера, можно изрисовать вообще всё!')

# Function definition block
def print_class_attribute_and_metod(my_class):
    print('\nКанцелярия относится к классу:', my_class.__class__.__name__)
    print('Наименование:', my_class.title)
    my_class.draw()

# initiate classes
print_class_attribute_and_metod(Pen())
print_class_attribute_and_metod(Pencil())
print_class_attribute_and_metod(Handle())