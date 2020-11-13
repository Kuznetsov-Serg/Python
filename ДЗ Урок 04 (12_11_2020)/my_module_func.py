'''
Курс: Основы языка Python
Урок 4. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
Модуль с собственными функциями
====================================================================
'''

# importing standard libraries
from sys import argv

def get_param (*args):
    '''
    A function of obtaining and analyzing the parameters of the run script.
    If the input is a list of keys, returns a dictionary with key values.
    Without a list of keys, returns a dictionary of input parameters numbered 1,2,3,..n
    :param args: - List (optionally)
    :return:
    '''
    param_list = argv.copy()        # copy the input parameters
    param_list.pop(0)               # delete the program name from parameters
    if len(args) == 0:              # list of key is empty
        # without a list of keys, returns a dictionary of input parameters numbered 1,2,3,..n
        param_dict = dict(zip(range(1, 100), param_list))   # fill in the dict
    else:
        key_list = args[0]
        # param_list = ['ggg', 'ddd', '3', 'ccc', ' ', '=', '999', '-b=', '888', '-rr', '=', '777','-r', '=33', '-h=666']
        param_str = ' '.join(param_list)
        param_dict = {x: get_value_by_key(param_str, x) for x in key_list}
    return param_dict

def get_value_by_key(my_str, key_str):
    # checking whether the key matches the text. for example,'- f 'matches' - f= ' or '- f = ' and '-flag'is not accepted
    point = my_str.find(key_str + ' =')             # search key
    if point == -1:                                 # not find
        point = my_str.find(key_str + '=')
        if point == -1:  # not find
            return ''
    point = my_str.find('=', point)                 # search start position of a value
    tmp_str = my_str[point + 1:].strip() + ' '      # cut out the string with the value and align it to the left
    point = tmp_str.find(' ')                       # search end position of a value
    tmp_str = tmp_str[:point]
    return tmp_str

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