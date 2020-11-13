'''
Курс: Основы языка Python
Урок 4. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
6)	Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
====================================================================
'''

# importing standard libraries
from itertools import count, cycle
import time

def generator1(start, step):
    for i in count(start, step):
        yield i

def generator2(my_list):
    for i in cycle(my_list):
        yield i

'''
script #1
iterator that generates integers starting from the specified one with the entered step
the condition for its completion is 10 iterations
'''
start = int(input('Введите первое число для генерации: '))
step = int(input('Введите шаг для генерации: '))
g1 = generator1(start, step)
for amount in range(2):
    for indx, el in enumerate(g1):
        print(el)
        if indx > 10:
            break
    print('*' * 50)
    time.sleep(2)
    # g1 = generator()     # обнуление ГЕНЕРАТОРА

'''
script #2
an iterator that repeats elements of a pre-defined list
the termination condition - 10 milliseconds
'''
# List of all even numbers from 5 to 20 (including borders)
my_list = [x for x in range(5, 20, 2)]

period_msec = 10            # exit after 10мс
g2 = generator2(my_list)
start_t = int(time.time() * 1000.0)
for indx, el in enumerate(g2):
    print(el)
    if start_t + period_msec < int(time.time()*1000.0):
        break
print('Прошло', period_msec, 'msec')

