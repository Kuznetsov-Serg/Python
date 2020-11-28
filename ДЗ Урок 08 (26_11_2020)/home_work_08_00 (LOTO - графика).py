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
from tkinter import *  # for graphics
import tkinter.ttk as ttk  # for ProgressBar
from time import sleep  # time for step limits


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
        len_field = 6  # len cells for the card
        str_separate = '-' * (9 * (len_field + 1) + 1) + '\n'  # separate line for good view
        out_str = str_separate
        for row in range(1, 4):  # three lines of the card
            out_str += '|'
            for col in range(1, 10):  # nine field in line of card
                cur_num = self.__find_num(row, col)  # let's find out what number is in this cell
                if cur_num != None:
                    if cur_num[1]:
                        cur_str = str(cur_num[0])  # if the number has not yet appeared in the game
                    else:
                        cur_str = '(' + str(cur_num[0]) + ')'  # if the number is already crossed out
                else:
                    cur_str = ''
                out_str += str(cur_str.center(len_field)) + '|'
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


# class for playing graphics
class ScreenLoto:
    def __init__(self):
        self.__flag_end_game = False  # flag the end of the game
        self.pc_card = Card()  # user's playing card
        self.my_card = Card()  # computer's playing card
        self.list_num = [i for i in range(1, 91)]  # putting numbers in the list
        self.root = Tk()
        self.root.title('Игра в ЛОТО')
        self.f_top = Frame(self.root)  # for Card
        self.f_but = Frame(self.root)  # for button
        self.f_bar = Frame(self.root)  # for ProgressBar
        desription_header = {'height': 1, 'anchor': 'nw', 'fg': 'red', 'font': ("Courier New", 16)}
        desription_card = {'height': 8, 'anchor': 'nw', 'fg': 'black', 'font': ("Courier New", 10)}
        # Frame CARD
        Label(self.f_top, text='Карта компьютера:', **desription_header).pack()
        self.card_pc = Label(self.f_top, text=str(self.pc_card), **desription_card)
        self.card_pc.pack()
        Label(self.f_top, text='Ваша карта:', **desription_header).pack()
        self.card_my = Label(self.f_top, text=str(self.my_card), **desription_card)
        self.card_my.pack()
        Label(self.f_top, text='Выпал бочонок № ', height=1, anchor='nw', font=("Courier New", 16)).pack(side=LEFT)
        self.current_num = Label(self.f_top, **desription_header)
        self.current_num.pack(side=LEFT)
        # Frame Button
        self.vin = Label(self.f_but, **desription_header)
        self.vin.pack(side=TOP)
        self.button_cross_num = Button(self.f_but, text=" Зачеркнуть в моей карточке ",
                                       command=lambda: self.next_num(True)).pack(side=RIGHT)
        self.button_next_step = Button(self.f_but, text=" Следующий бочонок ",
                                       command=lambda: self.next_num(False)).pack(side=RIGHT)
        self.__generate_num()
        # Frame ProgressBar
        self.progress_bar = ttk.Progressbar(self.f_bar, orient="horizontal", mode="determinate", maximum=100,
                                            value=0)
        self.progress_bar_name = Label(self.f_bar, text="Время для хода")
        self.progress_bar_name.grid(row=0, column=0)
        self.progress_bar.grid(row=0, column=1)
        # self.progress_bar.start()    # Start auto-incrementing periodically
        # self.progress_bar.step(100)  # The application
        self.f_top.pack()
        self.f_but.pack()
        self.f_bar.pack()
        self.root.update()
        while not self.__flag_end_game:
            self.progress_bar['value'] = 0
            while self.progress_bar['value'] < 100:
                self.progress_bar['value'] += 1
                self.root.update()
                sleep(0.1)
            self.next_num(False)
        # self.root.mainloop()

    def next_num(self, with_cross_num):
        cross_num = self.my_card.num_in_card(self.cur_num)
        if with_cross_num != cross_num or self.pc_card.card_is_finish():
            # user didn't notice the number in his card or mistaken or delete all numbers in the PC card
            self.print_vin('Вы ПРОИГРАЛИ!!!')
        elif self.my_card.card_is_finish():  # delete all numbers in the User card
            self.print_vin('Вы ВЫИГРАЛИ!!!')
        else:
            self.__generate_num()  # select the following random number
            self.progress_bar['value'] = 0
        # self.root.update()

    def __generate_num(self):  # select the following random number from remaining in List
        self.cur_num = self.list_num.pop(randint(0, len(self.list_num) - 1))
        self.current_num.config(text=str(self.cur_num))
        self.pc_card.num_in_card(self.cur_num)  # search number in the PC Card
        self.print_card()

    def print_card(self):
        self.card_pc.config(text=str(self.pc_card))
        self.card_my.config(text=str(self.my_card))
        self.root.update()

    def print_vin(self, vinner):
        self.vin.config(text=vinner)
        self.__flag_end_game = True
        self.progress_bar_name['text'] = 'Осталось до выхода из игры:'
        for i in range(0, 100, +3):
            self.progress_bar['value'] = i
            self.root.update()
            sleep(0.1)


# the code block of the program
screen_loto = ScreenLoto()
