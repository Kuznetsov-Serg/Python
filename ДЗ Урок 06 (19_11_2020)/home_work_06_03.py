'''
Курс: Основы языка Python
Урок 6. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
3)	Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
====================================================================
'''

class Worker:
    def __init__(self, name, surname, position, income_dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_dict = income_dict

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income_dict['wage'] + self._income_dict['bonus']

my_position1 = Position('Сергей', 'Кузнецов', 'младший помощник старшего дворника', {"wage": 10000, "bonus": 3000})
my_position2 = Position('Иван', 'Пупкин', 'Директор', {"wage": 50000, "bonus": 33000})

print(my_position1.get_full_name(), '(',my_position1.position, ') зарабатывает', my_position1.get_total_income())
print(my_position2.get_full_name(), '(',my_position2.position, ') зарабатывает', my_position2.get_total_income())
