'''
Курс: Основы языка Python
Урок 6. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
1)	Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
====================================================================
'''

# ВАРИАНТ №1
# import the standard functions
# from itertools import cycle
# from time import sleep
#
# class TrafficLight:
#     def __init__(self):
#         self.__colors = {'красный': 7, 'желтый': 2, 'зеленый': 4}      # private Dict (key - color, value - pause in sec)
#
#     def running(self):
#         for self.__color  in cycle(self.__colors):
#             print(self.__color)
#             sleep(self.__colors[self.__color])
#
# my_traffic_light = TrafficLight()
# my_traffic_light.running()

# ВАРИАНТ №2 (графический)

# import the standard functions
from random import *
from tkinter import *
from itertools import cycle
from time import sleep

# class description block
# the class "TRAFFIC light" (graphic design)
class TrafficLight:
    def __init__(self):         # initiating an instance of the class
        # traffic light dictionary: color: [duration (sec), coordinates x1, y1, x2, y2]
        self.__colors = {'red': [7, 100, 50, 200, 150], 'yellow': [2, 100, 160, 200, 260], 'green': [4, 100, 270, 200, 370]}      # private Dict (key - color, value - pause in sec)
        self.__flag_exit = False        # exit flag (by button)
        self.root = Tk()
        self.canvas = Canvas(self.root, width=300, height=470)
        self.canvas.create_rectangle(50, 10, 250, 410, fill = 'indigo', width = 5, outline = 'black')   # draw the traffic light case
        self.__gray_all_light()                                         # draw all segments of the traffic light in the inactive mode
        self.button_exit = Button(self.root, text=" Выход ")            # Button <Exit>
        self.button_exit.config(command=lambda: self.__exit())
        self.button_exit.pack(padx=30, pady=50)
        self.canvas.pack()

    def running(self):
        for self.__color in cycle(self.__colors):
            self.__gray_all_light()                 # draw all segments of the traffic light in the inactive mode
            self.canvas.create_oval(self.__colors[self.__color][1], self.__colors[self.__color][2], self.__colors[self.__color][3], self.__colors[self.__color][4], fill=self.__color, width = 5, outline = 'black')
            print(self.__color)                     # duplicate the traffic light signal in the console
            for cur_sec in range(self.__colors[self.__color][0]):   # хх second cycle
                self.root.title(self.__color+' ('+str(cur_sec)+' из '+str(self.__colors[self.__color][0])+'сек)')   # traffic light signal with duration-in the window title
                self.root.update()
                sleep(1)                    # pause 1 sec
                if self.__flag_exit:        # if the <Exit> button was pressed, then exit the method
                    exit(0)
            # you can uncomment it and use it without a loop, but then the <Exit> button will be less fast
            # sleep(self.__colors[self.__color][0])   # pause (xx sec)

    def __gray_all_light(self):     # draw all segments of the traffic light in the inactive mode
        for color in self.__colors:
            self.canvas.create_oval(self.__colors[color][1], self.__colors[color][2], self.__colors[color][3], self.__colors[color][4], fill='gray', width = 5, outline = 'black')

    def __exit(self):
        self.__flag_exit = True

my_traffic_light = TrafficLight()
my_traffic_light.running()
