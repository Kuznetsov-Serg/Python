'''
Курс: Основы языка Python
Урок 8. Знакомство с Python
Домашеннее задание (Кузнецов С.Н.)
====================================================================
== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
====================================================================
'''

# importing standard modules
from random import randint
from time import sleep


# Card class
class Card:
    def __init__(self):  # when creating an instance of the class, we will generate a game card
        my_list = self.generate_list_rnd(1, 90, 15)  # fill the list with random numbers without sorting
        self.card = {}  # dictionary for playing cards
        for row in range(1, 4):  # three lines of the card
            pos_list = self.generate_list_rnd(1, 9, 5, True)  # rnd positions of numbers in the line of the game card
            # inside the card line, numbers sort in ascending order
            self.card.update(
                {num: [True, row, col] for num, col in zip(sorted(my_list[(row - 1) * 5:(row - 1) * 5 + 5]), pos_list)})

    def __str__(self):
        color = Color()
        len_field = 6  # len cells for the card
        str_separate = '-' * (9 * (len_field + 1) + 1) + '\n'  # separate line for good view
        out_str = str_separate
        for row in range(1, 4):  # three lines of the card
            out_str += '|'
            for col in range(1, 10):  # nine field in line of card
                len_add = 0
                cur_num = self.__find_num(row, col)  # let's find out what number is in this cell
                if cur_num != None:
                    if cur_num[1]:
                        cur_str = color.RED + str(
                            cur_num[0]) + color.END  # if the number has not yet appeared in the game
                        len_add = len(color.RED + color.END)
                    else:
                        cur_str = '(' + str(cur_num[0]) + ')'  # if the number is already crossed out
                else:
                    cur_str = ''
                out_str += str(cur_str.center(len_field + len_add)) + '|'
            out_str += '\n' + str_separate
        return out_str

    def num_in_card(self, num):  # checking whether there is a number in the card
        if self.card.get(num) == None:
            return False
        else:
            self.card[num][0] = False  # cross out the number in the card
            return True

    def card_is_finish(self):  # checking whether all the numbers in the card are crossed out
        return True if sum(1 in x for x in self.card.values() if x[0]) == 0 else False

    @staticmethod
    def generate_list_rnd(low_range, hi_range, amount, sort=False):  # generating a unique list (set) with parameters
        my_set = set()
        while len(my_set) < amount:
            my_set.add(randint(low_range, hi_range))
        my_list = sorted(list(my_set)) if sort else list(my_set)
        return my_list

    def __find_num(self, row, col):  # the figure on the coordinate of the cell
        for key, val in self.card.items():
            if val[1] == row and val[2] == col:
                return (key, val[0])
        return None

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def yes_no_dialog(question, default_answer="yes"):
    answers = {"yes": 1, "y": 1, "ye": 1,
               "no": 0, "n": 0}
    if default_answer == None:
        tip = " [y/n] "
    elif default_answer == "yes":
        tip = " [Y/n] "
    elif default_answer == "no":
        tip = " [y/N] "
    else:
        raise ValueError(f'Неверное значение: {default_answer = }')
    while True:
        print(question + tip + ": ", end="")
        user_answer = input().lower()
        if default_answer is not None and user_answer == '':
            return answers[default_answer]
        elif user_answer in answers:
            return answers[user_answer]
        else:
            print("Пожалуйста, введите yes/y или no/n\n")


# the code block of the program
my_card = Card()
pc_card = Card()
num_list = [i for i in range(1, 91)]
pc_card_change = my_card_change = True
while len(num_list):
    if pc_card_change or my_card_change:
        print('Ваша карточка:\n', my_card)
        print('Карточка компьютера:\n', pc_card)
        if my_card.card_is_finish():
            print('Вы выиграли!!!')
            break
        if pc_card.card_is_finish():
            print('Компьютер выиграл!!!')
            break
    cur_num = num_list.pop(randint(0, len(num_list) - 1))
    pc_card_change = pc_card.num_in_card(cur_num)
    my_card_change = my_card.num_in_card(cur_num)
    my_answer = yes_no_dialog(f'На вашей карте есть цифра ({cur_num})?', 'no')
    if my_answer == 1 and my_card_change == False or my_answer == 0 and my_card_change == True:
        print('Вы ошиблись и ПРОИГРАЛИ!!!')
        break
