'''
Курс: Основы языка Python
Урок 5. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
6)	Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика:   100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
====================================================================
'''

import sys

def int_float_zero(in_str):
    '''
    The function tries to convert the argument to an integer or FLOAT. If it fails, returns 0.
    :param string: - any string, starting with numbers
    :return: - INT, FLOAT or Zero (not number)
    '''
    for ind, char in enumerate((in_str)):   # look through the entire line to the first non-numeric character
        if ('0' > char or char > '9') and char != '.':
            break
    else:
        ind += 1                            # all characters is numeric
    tmp_str = in_str[:ind]                  # delete the non-digital part
    if tmp_str.isdigit():
        return int(tmp_str)
    else:
        try:
            float(tmp_str)
            return float(tmp_str)
        except ValueError:
            return 0

def add_dict(in_str, in_dict):
    '''
    function for adding entries about a subject and its hours to the dictionary
    :param in_str:  - string with the name of the lesson and hours
    :param in_dict: - dictionary to add an entry to
    :return:
    '''
    my_list = in_str.split()
    lesson_name = my_list.pop(0)    # cut name of the lesson, and remain a list that includes strings starting with numbers
    amount_hour = sum([int_float_zero(hour) for hour in my_list])   # sum hours
    if in_dict.get(lesson_name) == None:        # checking for presence in the dictionary
        in_dict[lesson_name] = amount_hour      # adding a new element
    else:
        in_dict[lesson_name] += amount_hour     # adding new hours for the subject

'''
the program processes the file
and gets lines from it with the name of the lesson and the hours
at the output-a dictionary with the types of lessons and the sum of hours for each
'''
f_name = "home_work_05_06.txt"
my_dict = {}
try:
    with open(f_name) as f_obj:      # open the file and get the contents
        input_list = f_obj.readlines()
    print('Из файла', f_name, 'считали:')
    {print(in_str, end=''): add_dict(in_str, my_dict) for in_str in input_list}
    print('\nПолучили словарь:\n', my_dict)
except IOError:
    print("Произошла ошибка ввода-вывода!")
    sys.exit(1)

