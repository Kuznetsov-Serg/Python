'''
Курс: Основы языка Python
Урок 2. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
2)	Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
====================================================================
'''
# Функция реверса передавамого списка
def list_convert_12(base_list):
    tmp_list = base_list.copy()             # список передается по адресу, чтобы не испортить - клонируем (копируем) в новый список
    for el in range(len(tmp_list) // 2):
        current = tmp_list.pop(el * 2)
        tmp_list.insert(el * 2 + 1, current)
    return (tmp_list)

# Блок создания и объявления переменных

string = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
my_list = list(string)  # Заполним базовый список
print('Первоначальный список:\n', my_list)
result_list = list_convert_12(my_list)
print('Список с замещенными значениями:\n', result_list)
my_list.pop()
print('Проверим на нечетном количестве, убрав последний элемент:\n', my_list)
result_list = list_convert_12(my_list)
print('Список с замещенными значениями:\n', result_list)





