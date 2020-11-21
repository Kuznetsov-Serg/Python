'''
Курс: Основы языка Python
Урок 6. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
4)	Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
====================================================================
'''

# Class definition block
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(self.name, 'поехала')
    def stop(self):
        print(self.name, 'остановилась')
    def turn(self, direction):
        print(self.name, 'повернула', direction)
    def show_speed(self):
        print('Текущая скорость автомобиля', self.name, 'составляет', self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Внимание, превышение скорости!!!')
        super().show_speed()                        # next, as in the parent class

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Внимание, превышение скорости!!!')
        super().show_speed()                        # next, as in the parent class

class SportCar(Car):            # Synonym of the parent class
    pass
class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)     # initializing the parent class with the current list of parameters + is_police

# Function definition block
def print_car_attribute_and_metod(my_car):
    print('\nАвтомобиль относится к классу:', my_car.__class__.__name__)
    print('Наименование:', my_car.name)
    print('Цвет:',my_car.color)
    if my_car.is_police:
        print('(это автомобиль полиции)')
    my_car.go()
    my_car.show_speed()

# initiate instances of classes TownCar, SportCar, WorkCar, PoliceCar
print_car_attribute_and_metod(TownCar(70, 'green', 'Toyota'))
print_car_attribute_and_metod(SportCar(90, 'yellow', 'Honda'))
print_car_attribute_and_metod(WorkCar(40,'red', 'Volvo'))
print_car_attribute_and_metod(PoliceCar(120, 'white', 'mazda RX-5'))
