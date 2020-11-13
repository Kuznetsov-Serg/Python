'''
Курс: Основы языка Python
Урок 4. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
7)	Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
====================================================================
'''

# importing standard libraries
import math

def fact():
    i = 0
    while True:
        i += 1
        yield math.factorial(i)

n = int(input('Введите n: '))
g = fact()
for indx, el in enumerate(g, 1):
    print('{}! = {}' .format(indx, el))
    if indx >= n:
        break

# importing standard libraries
# from itertools import count, cycle

# def generator():
#     i = 0
#     while True:
#         i += 1
#         yield i
#
# def fact(n):
#     g = generator()
#     result = 1
#     for indx, el in enumerate(g):
#         result *= el
#         if el == n:
#             return result
#
# print(fact(4))
