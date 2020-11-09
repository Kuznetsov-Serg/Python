'''
Курс: Основы языка Python
Урок 1. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
1)	Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
====================================================================
'''

# объявляем функцию диалога
# question – это вопрос, который выводится в командную строку,
# и на который пользователь должен дать ответ “yes” или “no”.
# default_ answer – это необязательный параметр, который будет
# использоваться в том случае, если пользователь не введет ответ, а просто нажмет Enter

def yes_no_dialog(question, default_answer="yes"):
    answers = {"yes":1, "y":1, "ye":1,
        "no":0, "n":0}
    if default_answer == None:
        tip = " [y/n] "
    elif default_answer == "yes":
        tip = " [Y/n] "
    elif default_answer == "no":
        tip = " [y/N] "
    else:
        raise ValueError(f'Неверное значение: {default_answer = }')
    while True:
        print(question + tip + ": ", end="")
        user_answer = input().lower()
        if default_answer is not None and user_answer == '':
            return answers[default_answer]
        elif user_answer in answers:
            return answers[user_answer]
        else:
            print("Пожалуйста, введите yes/y или no/n\n")

#import tkinter

# Блок создания и объявления переменных
first_name = 'Сергей'
last_name = 'Кузнецов'
age = 46
pi = 3.14
is_man = True

# Вывод на экран
print('Имя: {0}\nФамилия: {1}\nВозраст: {2} лет \nмужской пол [{3}]' .format(first_name,last_name, age,is_man))

# Расчет площади круга
circle_radius = float(input('Введите радиус круга для рассчета его площади: '))
circle_area = pi * circle_radius ** 2
print('Площадь круга составляет %.2f'% circle_area)

# Запрашиваем ФИО и пол для последующего вывода на экран
fio = input('Введите ФИО:')
if yes_no_dialog('Пол мужской?') == 1:
    is_man = True
else:
    is_man = False
print('ФИО {}\nмужской пол [{}]' .format(fio,is_man))






