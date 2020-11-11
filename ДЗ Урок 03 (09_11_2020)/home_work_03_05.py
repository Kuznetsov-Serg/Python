'''
Курс: Основы языка Python
Урок 3. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
5)	Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
====================================================================
'''

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

# declaring initializing variables
result_list = []        # list of numbers
flag_exit = -1          # flag end of program
while flag_exit < 0:
    # my_str = '10 20 333 9999 67.9887 78.99 778,99 Q 987654'
    my_str = input('Введите строку чисел, разделенных пробелом ("q" для завершения): ')
    my_str = my_str.lower()     # lower case for ease search 'q'
    flag_exit = my_str.find('q')
    if flag_exit > 0:
        my_str = my_str[:flag_exit-1]   # cut off from 'q'
    my_list = my_str.split(' ')         # move str to the list
    result_list.extend(list(map(lambda x: int_float_zero(x), my_list)))  # converts STR to INT or FLOAT and adds it to the result_list
    print(result_list)
    print(sum(result_list))




