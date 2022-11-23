import sympy as sp
from tkinter import *

import Window_form


def calculate(funk, x_min, x_max, k):
    # Объявление переменных
    step = 0
    text = ""
    x = sp.symbols('x')

    funk = sp.parse_expr(funk)
    x1 = x_max
    x0 = x_min

    # Выполняем k-1 шагов
    for i in range(1, k):
        # Нахождение точек, в которых будут вычисляться значения функции
        right = x_min + ((numb_Fibonacci(k + 1 - i) / numb_Fibonacci(k + 1)) * (x1 - x0))
        left = x_min + ((numb_Fibonacci(k - i) / numb_Fibonacci(k + 1)) * (x1 - x0))
        # Подстановка в функцию значений и сравнивание полученных значений
        if funk.subs(x, right) > funk.subs(x, left):
            x_max = right
        else:
            x_min = left
        step += 1
    # Вывод результатов
        text += Window_form.print_steps(step, x_min, x_max, funk.subs(x, x_min), funk.subs(x, x_max))
    if k == 1:
        text += Window_form.print_steps(1, x_min, x_max, funk.subs(x, x_min), funk.subs(x, x_max))
    text += Window_form.print_result(step, x_min, x_max, funk.subs(x, x_min), funk.subs(x, x_max))
    Window_form.result.insert(INSERT, text)


# Функция нахождения числа Фибоначчи
def numb_Fibonacci(n):
    n0 = 1
    n1 = 1
    numb_fibon = 0
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n + 1):
            numb_fibon = n0 + n1
            n0 = n1
            n1 = numb_fibon
        return numb_fibon
