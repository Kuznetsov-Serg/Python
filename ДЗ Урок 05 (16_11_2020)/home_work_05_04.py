'''
Курс: Основы языка Python
Урок 5. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
====================================================================
'''

import sys

def replace_eng_rus(in_str):
    '''
    Function for replacing English numerals in a string with their Russian translation
    :param in_str:  - string that includes English numerals
    :return:        - string with translation of numerals into Russian
    '''
    in_list = list(in_str.lower().split())                      # converting a string to a list
    out_list = [replace_from_eng_dict(out) for out in in_list]  # attempt to replace each word with Russian words from the dictionary
    return ' '.join(out_list)                                   # converting a list to a string

def replace_from_eng_dict(in_str):
    '''
    Function for replacing a word with a translation if it is available in the dictionary
    :param in_str:
    :return:
    '''
    eng_rus_dict = {'one': 'Один', 'two': 'Два', 'three': 'Три', 'four': 'Четыре', 'five': 'Пять', 'six': 'Шесть',
                    'seven': 'Семь', 'eight': 'Восемь', 'nine': 'Девять', 'zero': 'Ноль'}
    out_str = in_str if eng_rus_dict.get(in_str) == None else eng_rus_dict.get(in_str)
    return out_str

f_name = "home_work_05_04.txt"
try:
    with open(f_name) as f_obj:      # open the file and get the contents
        input_list = f_obj.readlines()
    print('Из файла', f_name, 'считали:')
    [print(in_str, end='') for in_str in input_list]
except IOError:
    print("Произошла ошибка ввода-вывода!")
    sys.exit(1)

new_list = [replace_eng_rus(input_str) + '\n' for input_str in input_list]
f_name = "home_work_05_04_out.txt"
try:
    with open(f_name, 'w', encoding='utf-8') as f_obj:   # open the file and put the contents
        f_obj.writelines(new_list)
    print('\n\nВ файл', f_name, 'записали:')
    [print(in_str, end='') for in_str in new_list]
except IOError:
    print("Произошла ошибка ввода-вывода!")
    sys.exit(1)
