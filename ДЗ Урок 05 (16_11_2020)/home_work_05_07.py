'''
Курс: Основы языка Python
Урок 5. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
====================================================================
'''

# importing standard modules
import sys
import statistics
import json

# function description block
def int_float_zero(in_str):
    '''
    The function tries to convert the argument to an integer or FLOAT. If it fails, returns 0.
    :param string: - any string, starting with numbers
    :return: - INT, FLOAT or Zero (not number)
    '''
    for ind, char in enumerate((in_str)):   # look through the entire line to the first non-numeric character
        if ('0' > char or char > '9') and char != '.':
            break
    else:
        ind += 1                            # all characters is numeric
    tmp_str = in_str[:ind]                  # delete the non-digital part
    if tmp_str.isdigit():
        return int(tmp_str)
    else:
        try:
            float(tmp_str)
            return float(tmp_str)
        except ValueError:
            return 0

def add_dict(in_str, in_dict):
    '''
    function for adding entries about a subject and its hours to the dictionary
    :param in_str:  - string with the name of the company, form of ownership, revenue and expenses
    :param in_dict: - dictionary to add an entry to
    :return:
    '''
    my_list = in_str.split()
    expenses = int_float_zero(my_list.pop())    # cut expenses
    revenue = int_float_zero(my_list.pop())     # cut revenue
    form_of_business = my_list.pop()            # form of business
    name = ' '.join(my_list)                    # name
    profit = revenue - expenses                 # profit
    in_dict[name] = profit                      # adding a new element in the dictionary

'''
the program processes the file
each line contains a record with the name of the company, form of business, revenue and expenses
the name of an organization can consist of several words, for example: ('Рога и копыта', 'МБОУ №16', 'Кузнецов Сергей Николаевич')
the program generates a list [dictionary with firms and their profits/loss, dictionary average profit]
The final list is saved as a json object to a file.
'''
f_name = "home_work_05_07.txt"
my_dict = {}
try:
    with open(f_name) as f_obj:      # open the file and get the contents
        input_list = f_obj.readlines()
    print('Из файла', f_name, 'считали:')
    {print(in_str, end=''): add_dict(in_str, my_dict) for in_str in input_list}
    average_profit = statistics.mean([x for x in my_dict.values() if x > 0])     # average profit excluding firms with a loss
    my_list = [my_dict, {'average_profit': average_profit}]
    print('\n\nПолучили список:\n', my_list)
except IOError:
    print("Произошла ошибка ввода-вывода!")
    sys.exit(1)

f_name = "home_work_05_07.json"
with open(f_name, 'w', encoding='utf-8') as f_json:
    json.dump(my_list, f_json, ensure_ascii=True, indent=4)

with open(f_name) as f_json:
    data_loaded = json.load(f_json)
print('\nВ файле', f_name, 'сохранены данные:\n', data_loaded)
