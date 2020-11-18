'''
Курс: Основы языка Python
Урок 5. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
5)	Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
====================================================================
'''

'''
The program asks for the numbers, separated by a space.
Writes the entered string to a file.
Calculates and outputs the sum of numbers.
You can enter integers, FLOAT, and other types as strings.
Examples of strings:
'10 11,55 88.789 33.00 aaa 987 89.09'
'44 77 99 33 0 18.99'
'''

import sys

def int_float_zero(string):
    '''
    The function tries to convert the argument to an integer or FLOAT. If it fails, returns 0.
    :param string: - any string
    :return: - INT, FLOAT or Zero (not number)
    '''
    if string.isdigit():
        return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return 0

# input_str = '10 11,55 88.789 33.00 aaa 987 89.09'
input_str = input('Введите набор чисел, разделенных пробелами: ')
input_list = input_str.split()
digit_list = [int_float_zero(x) for x in input_list]  # converts STR to INT or FLOAT and adds it to the result_list
f_name = "home_work_05_05.txt"
try:
    with open(f_name, 'w', encoding='utf-8') as f_obj:   # open the file for put the contents
        f_obj.write(input_str)
        f_obj.write('\nСумма чисел составляет: ' + str(sum(digit_list)))
    print('\nВы ввели:', input_str, '\nв качестве чисел принят список:', digit_list, '\nСумма чисел составляет: ', sum(digit_list), '\nРезультат записан в файл', f_name)
except IOError:
    print("Произошла ошибка ввода-вывода!")
    sys.exit(1)
