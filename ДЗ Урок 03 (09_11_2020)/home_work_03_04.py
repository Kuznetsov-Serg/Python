'''
Курс: Основы языка Python
Урок 3. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
4)	Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
====================================================================
'''

def exponentiation(num, degree):
    '''
    Function of exponentiation. (recursion)
    :param num: - any number (positive, negative, integer, FLOAT,...)
    :param degree: - integer (positive or negative)
    :return:
    EXAMPLES:
    >>>raise_degree(2, 4)
    16
    >>>raise_degree(-2.5, 4)
    39.0625
    >>>raise_degree(2, -4)
    0.0625
    '''
    if degree == 0:
        return 1        # any number exponentiation 0 s equal to 1
    elif degree > 0:
        return (num * exponentiation(num, degree-1))  # recursion with decreasing exponentiation
    else:
        return (1/(num * exponentiation(num, abs(degree)-1)))     # negative exponentiation

print('Проверка:')
print('2 в степени 4 =', exponentiation(2, 4), 'встроенная функция', 2**4)
print('-2.5 в степени 4 =', exponentiation(-2.5, 4), 'встроенная функция', (-2.5)**4)
print('2 в степени -4 =', exponentiation(2, -4), 'встроенная функция', 2**-4)
