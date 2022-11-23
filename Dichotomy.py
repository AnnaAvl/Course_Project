from tkinter import *
from tkinter import messagebox
import sympy as sp

import Window_form


def calculate(funk, x_min, x_max, delta, e):
    if delta * 2 >= e:
        messagebox.showerror("Ошибка", "\u03B5 <= 2 * \u0394")
        return
    # Объявление переменных
    step = 0
    text = ""
    x = sp.symbols('x')
    funk = sp.parse_expr(funk)
    # Пока отрезок больше заданной погрешности
    while abs(x_max - x_min) >= e:
        # Нахождение точек, в которых будут вычисляться значения функции
        right = ((x_max + x_min) / 2) + delta
        left = ((x_max + x_min) / 2) - delta
        # Подстановка в функцию значений и сравнивание полученных значений
        if funk.subs(x, right) > funk.subs(x, left):
            x_max = right
        else:
            x_min = left
        step += 1
    # Вывод результатов
        text += Window_form.print_steps(step, x_min, x_max, funk.subs(x, x_min), funk.subs(x, x_max))
    text += Window_form.print_result(step, x_min, x_max, funk.subs(x, x_min), funk.subs(x, x_max))
    Window_form.result.insert(INSERT, text)
