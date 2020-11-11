'''
Курс: Основы языка Python
Урок 3. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
3)	Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
====================================================================
'''

def my_func(*args):
    '''
    The function accepts two or more positional arguments,
    and returns the sum of the largest two arguments.
    :param args:
    :return:
    '''
    if len(args) < 2:
        print('Вызов функции не имеет смысла, т.к. аргументов менее 2-х')
        return
    my_list = []
    my_list.extend(args)
    print(my_list)
    my_list.sort(reverse=True)
    return (my_list[0] + my_list[1])

print(my_func(10, 20, 30, 40))
print(my_func(10, 11, 24.7, 17, 70, -12, 10))
print(my_func('aaa', 'bb', 'ccccc', 'd'))

# Вариант 2 с использованием Анонимной функции (lambda)
# Ограничеия - количсетво аргументов - 3шт и только числовые занчения
my_func2 = lambda *args: sum(args) - min(args)
print(my_func2(10, 20, 30))
print(my_func2(10, -20, 30))
print(my_func2(10.2, 20.7, 30.9))








