'''
Курс: Основы языка Python
Урок 5. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
1)	Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
====================================================================
'''

try:
    with open("home_work_05_01.txt", 'w', encoding='utf-8') as f_obj:
        while True:
            content = input("Введите очередную строку (для завершения ''): ")
            if content == '':
                break
            f_obj.write(content + '\n')
except IOError:
    print("Произошла ошибка ввода-вывода!")

try:
    with open("home_work_05_01.txt", 'r', encoding='utf-8') as f_obj:
        while True:
            content = f_obj.read(1024)
            print(content)
            if not content:
                break
        # print(f_obj.readlines())
except IOError:
    print("Произошла ошибка ввода-вывода!")



