'''
Курс: Основы языка Python
Урок 3. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
2)	Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
====================================================================
'''

def card_print(name, surname, year_born = 0, city = '', email = '', tel = ''):
    '''
    The function accepts several parameters (named arguments).
    Some of the parameters are required.
    The employee card contains only the received field names and their values (printed in one line)
    :param name: - required parameter
    :param surname: - required parameter
    :param year_born:
    :param city:
    :param email:
    :param tel:
    :return:
    '''
    card_dict = {}
    card_dict['Имя'] = name         # required parameter
    card_dict['Фамилия'] = surname  # required parameter

    if year_born != 0:
        card_dict['Год рождения'] = year_born
    if city != '':
        card_dict['Город проживания'] = city
    if email != '':
        card_dict['Email'] = email
    if tel != '':
        card_dict['Тел'] = tel
    print(card_dict)


card_print(name='Sergey', surname='Kuznetsov', year_born=1974, city='SaintPetersburg', email='ksn1974@mail.ru',tel='8-999-209-0008')
card_print(surname='Pupkin', name='Ivan', year_born=1991)
card_print(name='Vasilisa', surname='Ivanova')
card_print(name='Vlada', surname='Durakova', year_born=2007, city='Moscow', tel='8 (495) 337-22-88')

