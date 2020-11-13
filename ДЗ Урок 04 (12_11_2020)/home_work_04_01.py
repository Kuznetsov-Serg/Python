'''
Курс: Основы языка Python
Урок 4. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
1)	Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
====================================================================
'''
'''
script with the function of calculating the employee's salary
formula: (output in hours*rate per hour) + bonus
To perform a calculation for specific values, you need to run a script with parameters.
The script is not sensitive to the rules for placing spaces and the order of parameters!!!
The examples run
>>> python home_work_04_01.py ggg ddd 3 ccc   = 999 -b= 888 -rr = 777 -r =33 -h=666
Зарплата сотрудника составит - 22,866.00
>>> python home_work_04_01.py -h = 10 -r=20 -b= 40
Зарплата сотрудника составит - 240.00
'''
import my_module_func as my             # importing my module


# print(my.get_param())     # without a list of keys, returns a dictionary of input parameters numbered 1,2,3,..n
key_list = ['-h', '-r', '-b']                           # list of key parameters
param_dict = my.get_param(key_list)                     # get a dictionary of named input parameters

hours_worked = my.int_float_zero(param_dict['-h'])      # hours worked
rate = my.int_float_zero(param_dict['-r'])              # Rate per hour
bonus = my.int_float_zero(param_dict['-b'])             # bonus

print('При входных параметрах:\nВыработка - {} час\nСтавка в час - {}\nПремия - {}\nЗарплата сотрудника составит - {:,.2f}' .format(hours_worked, rate, bonus, hours_worked * rate + bonus))






