'''
Курс: Основы языка Python
Урок 5. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
3)	Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
====================================================================
'''

try:
    with open("home_work_05_03.txt") as f_obj:
    # with open("home_work_05_03.txt", 'r', encoding='utf-8') as f_obj:
        content_list = f_obj.readlines()
except IOError:
    print("Произошла ошибка ввода-вывода!")

# fill in the dictionary with employees and salaries
my_dict = {my_str.split()[0]: float(my_str.split()[1]) for my_str in content_list}

salary_level = 20000    # salary level below which we print employees
print('Список сотрудников с окладом ниже {:,.2f}' .format(salary_level))
[print('{:15}  {:10,.2f}'.format(name, salary)) for name, salary in my_dict.items() if salary < salary_level]

salary_all = sum(my_dict.values())      # total amount of salaries
count = len(my_dict)                    # number of salary entries
print('Исходя из общей суммы {:,.2f} на {} сотрудников, средняя велечина дохода составляет {:,.2f}' .format(salary_all, count, salary_all/count))

