'''
Курс: Основы языка Python
Урок 3. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
1)	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
====================================================================
'''

def division_func(arg_1, arg_2):
    '''
    The function of the division.
    :param arg_1: - dividend (numerator)
    :param arg_2: - divider (denominator)
    :return:
    There is a processing of the situation of division by zero and input of non-digital arguments.
    '''
    try:
        float(arg_1)
        float(arg_2)
        return (arg_1 / arg_2)
    except ValueError:
        print('Введено не число!')
    except ZeroDivisionError:
        print('На НОЛЬ делить нельзя!')

def int_float_str(string):
    '''
    The function tries to convert the argument to an integer or FLOAT. If it fails, returns the original string.
    :param string: - any string
    :return: - INT, FLOAT or STR
    '''
    if string.isdigit():
        return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return string


num_1 = int_float_str(input('Введите делимое: '))
num_2 = int_float_str(input('Введите делитель: '))
print(division_func(num_1, num_2))









