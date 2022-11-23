import math

import sympy as sp
from tkinter import *

import Window_form


def calculate(funk, x_min, x_max, e):
    # Объявление переменных
    step = 0
    text = ""
    # Константа
    t = (1 + math.sqrt(5)) / 2
    x = sp.symbols('x')
    funk = sp.parse_expr(funk)

    # Пока отрезок больше заданной погрешности
    while abs(x_max - x_min) >= e:
        # Нахождение точек, в которых будут вычисляться значения функции
        x2 = x_min + (x_max - x_min) / t
        x1 = x_max - (x_max - x_min) / t
        # Подстановка в функцию значений и сравнивание полученных значений
        if funk.subs(x, x1) >= funk.subs(x, x2):
            x_min = x1
        else:
            x_max = x2
        step += 1
    # Вывод результатов
        text += Window_form.print_steps(step, x_min, x_max, funk.subs(x, x_min), funk.subs(x, x_max))
    text += Window_form.print_result(step, x_min, x_max, funk.subs(x, x_min), funk.subs(x, x_max))
    Window_form.result.insert(INSERT, text)
