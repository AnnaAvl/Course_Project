import random

import sympy as sp

import Window_form
from tkinter import *


def calculate(funk, x_min, x_max, k):
    # Объявление переменных
    step = 0
    text = ""
    d = dict()
    x = sp.symbols('x')
    funk = sp.parse_expr(funk)


    # Пока кол-во точек не достигнет заанного
    while len(d.keys()) != k:
        x_i = random.uniform(x_min, x_max)  # Выбор рандомного числа из отрезка
        funk_i = funk.subs(x, x_i)  # Подстановка в функцию
        d.update({x_i: funk_i})  # Добавление в словарь (Особенность: не добавляет повторные значения ключей)
        step += 1
    # Вывод результатов
        text += str(step) + ") xi = " + str(x_i) + ", Funk_i = " + str(funk_i) + "\n"
    text += "\nМинимум функции равен " + str(min(d.values())) + " и достигается в точке " + str(
        list(d.keys())[list(d.values()).index(min(d.values()))]) + "\n" + "Количество шагов: " + str(step)
    Window_form.result.insert(INSERT, text)
