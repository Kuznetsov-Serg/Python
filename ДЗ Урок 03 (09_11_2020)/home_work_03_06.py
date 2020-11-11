'''
Курс: Основы языка Python
Урок 3. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
6)	Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
====================================================================
'''

def ucase_word(in_str):
    '''
    the function is analogous to the method .title()
    accepts a word and returns the same word, but with the first letter uppercase
    :param in_str: - any word
    :return: - Word with the first letter uppercase
    '''
    char = in_str[0]                    # take the first character
    if char >= 'a' and char <= 'z':
        char = chr(ord(char)-32)        # change to the same character, but in uppercase
    if char >= 'а' and char <= 'п':
        char = chr(ord(char)-32)
    if char >= 'р' and char <= 'я':
        char = chr(ord(char)-(ord('р')-ord('Р')))
    return char + in_str[1:]            # return the word with the first letter in uppercase

def ucase_sentence(in_str):
    '''
    This function sends all the words of the received sentence to the ucase_word function.
    :param in_str: - words separated by spaces (sentence)
    :return:    - returns the sentence received as an argument (all words start with an uppercase letter)
    '''
    return (' '.join(list(map(lambda x: ucase_word(x), in_str.split(' ')))))

# examples of how functions work
my_str = 'sergey'
print(my_str, '\n(после обработки методом)', my_str.title(), '\n(после обработки самопальной функцией)', ucase_word(my_str), '\n')

my_str = 'sergey, lena and valery - programmers'
print(my_str, '\n(после обработки методом)', my_str.title(), '\n(после обработки самопальной функцией)', ucase_sentence(my_str), '\n')

my_str = 'алексей и сергей учатся в школе geekbrain на программистов'
print(my_str, '\n(после обработки методом)', my_str.title(), '\n(после обработки самопальной функцией)', ucase_sentence(my_str), '\n')

# launch functions with parameters entered in the console
my_str = input('Введите одно слово в нижнем регистре: ')
print(my_str, '\n(после обработки методом)', my_str.title(), '\n(после обработки самопальной функцией)', ucase_word(my_str), '\n')

my_str = input('Введите строку слов в нижнем регистре: ')
print(my_str, '\n(после обработки методом)', my_str.title(), '\n(после обработки самопальной функцией)', ucase_sentence(my_str), '\n')
