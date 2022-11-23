from tkinter import *
from tkinter import messagebox, scrolledtext
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
import sympy as sp

import Dichotomy
import Fibonacci
import Golden_ratio
import Monte_Carlo


# Функция проверки на ввод позитивного дробного числа
def validate_pos_float(new_value):
    return new_value == "" or new_value.replace('.', '', 1).isdigit()


# Ошибка при не соответствии условиям validate_pos_float()
def print_pos_float_error():
    messagebox.showerror('Ошибка', 'Введите дробное позитивное число (через точку)')


# Функция проверки на ввод любого дробного числа
def validate_all_float(new_value):
    return new_value == "" or new_value.replace('.', '', 1).isdigit() or (new_value[0] == "-" and (
            new_value.replace('-', '', 1) == "" or new_value.replace('-', '', 1).replace('.', '', 1).isdigit()))


# Ошибка при не соответствии условиям validate_all_float()
def print_all_float_error():
    messagebox.showerror('Ошибка', 'Введите дробное число (через точку)')


# Функция проверки на ввод позитивного целого числа
def validate_int_positive(new_value):
    return new_value == "" or (new_value.isdigit() and int(new_value) > 0)


# Ошибка при не соответствии условиям validate_int_positive()
def print_positive_error():
    messagebox.showerror('Ошибка', 'Введите целое позитивное число')


# Ошибка при не соответствии условию Xmin < Xmax
def print_x_error():
    messagebox.showerror("Ошибка", "Xmin >= Xmax")


# Ошибка при не введенных данных
def print_error():
    messagebox.showerror("Ошибка", "Заполните все исходные данные")


# Функция отрисовки доп. полей при выборе метода
def selected(event):
    method = combobox_method.current()
    # Удаление ранее отрисованных доп. элементов
    for i in temp_elements:
        i.grid_remove()
    # Отображение доп. элементов в соответствии с выбранным методом
    if method == 0:
        lbl_k.grid(column=2, row=3, sticky=E)
        k.delete(0, END)
        k.grid(column=3, row=3, sticky=W)
    elif method == 1:
        lbl_delta.grid(column=2, row=3, sticky=E)
        lbl_e.grid(column=2, row=4, sticky=E)
        delta.delete(0, END)
        delta.grid(column=3, row=3, sticky=W)
        e.delete(0, END)
        e.grid(column=3, row=4, sticky=W)
    elif method == 2:
        lbl_e.grid(column=2, row=3, sticky=E)
        e.delete(0, END)
        e.grid(column=3, row=3, sticky=W)
    elif method == 3:
        lbl_k.grid(column=2, row=3, sticky=E)
        k.delete(0, END)
        k.grid(column=3, row=3, sticky=W)


# Функция рассчета
def clicked():
    # Проверка того, что все поля заполнены
    if funk.get() == "" or x_min.get() == "" or x_max.get() == "" or combobox_method.current() == -1:
        print_error()
        return
    # Проверка границ отрезка
    elif float(x_min.get()) >= float(x_max.get()):
        print_x_error()
        return
    # Проверка того, что введенная функция корректна
    else:
        try:
            x = sp.symbols('x')
            funktion = sp.parse_expr(funk.get())
            float(funktion.subs(x, x_min.get()))
        except:
            messagebox.showerror("Ошибка", "Функция введена некорректно")
            return
    if combobox_method.current() == 0:
        # Проверка того, что все доп. поля заполнены
        if k.get() == "":
            print_error()
        else:
            # Устанавливаем поле результата в состояние записи
            result.config(state=NORMAL)
            # Очищаем поле результата
            result.delete(1.0, END)
            # Вызов метода подсчета
            Monte_Carlo.calculate(funk.get(), float(x_min.get()), float(x_max.get()), int(k.get()))
            # Блокируем поле результата
            result.config(state=DISABLED)
    elif combobox_method.current() == 1:
        if delta.get() == "" or e.get() == "":
            print_error()
        else:
            global coma
            coma = len(delta.get().split(".")[1])
            result.config(state=NORMAL)
            result.delete(1.0, END)
            Dichotomy.calculate(funk.get(), float(x_min.get()), float(x_max.get()), float(delta.get()), float(e.get()))
            result.config(state=DISABLED)
    elif combobox_method.current() == 2:
        if e.get() == "":
            print_error()
        else:
            coma = len(e.get().split(".")[1])
            result.config(state=NORMAL)
            result.delete(1.0, END)
            Golden_ratio.calculate(funk.get(), float(x_min.get()), float(x_max.get()), float(e.get()))
            result.config(state=DISABLED)
    elif combobox_method.current() == 3:
        if k.get() == "":
            print_error()
        else:
            result.config(state=NORMAL)
            result.delete(1.0, END)
            Fibonacci.calculate(funk.get(), float(x_min.get()), float(x_max.get()), int(k.get()))
            result.config(state=DISABLED)


# Функция, формирующая строку с шагом
# Значение funk_max - значение функции в точке xmax, funk_min - в точке xmin
def print_steps(step, xmin, xmax, funk_min, funk_max):
    return str(step) + ") xmin = " + str(round(xmin, coma)) + ", xmax = " + str(
        round(xmax, coma)) + "; minFunk = " + str(round(funk_min, coma)) + ", maxFunk = " + str(
        round(funk_max, coma)) + "\n"


# Функция, формирующая строку результата
def print_result(step, xmin, xmax, funk_min, funk_max):
    if funk_min > funk_max:
        return "\nМинимум функции равен " + str(round(funk_max, coma)) + " и достигается в точке " + str(
            round(xmax, coma)) + "\n" + "Количество шагов: " + str(step)
    else:
        return "\nМинимум функции равен " + str(round(funk_min, coma)) + " и достигается в точке " + str(
            round(xmin, coma)) + "\n" + "Количество шагов: " + str(step)


# Функция загрузки данных из файла
def read_datafile():
    # Уточняем, что переменная глобальная, чтобы присвоить ей значение, которое будет использоваться в др. функции
    global file_name
    # Указывваем расширение файлов, которые буут отображаться в диалогом окне
    file_name = fd.askopenfilename(filetypes=[("Text files", "*.txt")])
    # Проверяем выбран ли файл
    if file_name == "":
        return
    # Открываем файл для чтения
    f = open(file_name, 'r', encoding='utf-8')
    # Разделяем данные по переносу на массив
    data = f.read().split("\n")
    # Очищаем поля
    # Записываем данные, выделяя в каждом элементе массива часть после знака  "="
    funk.delete(0, END)
    funk.insert(0, data[0].split(" = ")[1])
    x_min.delete(0, END)
    x_min.insert(0, data[1].split(" = ")[1])
    x_max.delete(0, END)
    x_max.insert(0, data[2].split(" = ")[1])
    method = data[3].split(" = ")[1]
    # В зависимости от выбранного метода, записываем доп. данные
    if method == "Монте-Карло":
        selected(combobox_method.current(0))
        k.delete(0, END)
        k.insert(0, data[4].split(" = ")[1])
    elif method == "Дихотомии":
        selected(combobox_method.current(1))
        delta.delete(0, END)
        delta.insert(0, data[4].split(" = ")[1])
        e.delete(0, END)
        e.insert(0, data[5].split(" = ")[1])
    elif method == "Золотого сечения":
        selected(combobox_method.current(2))
        e.delete(0, END)
        e.insert(0, data[4].split(" = ")[1])
    elif method == "Фибоначчи":
        selected(combobox_method.current(3))
        k.delete(0, END)
        k.insert(0, data[4].split(" = ")[1])


# Функция записи данных в файл
def write_datafile():
    # Проверка того, что все поля заполнены
    if funk.get() == "" or x_min.get() == "" or x_max.get() == "" or combobox_method.current() == -1:
        print_error()
        return
    # Проверка границ отрезка
    elif float(x_min.get()) > float(x_max.get()):
        print_x_error()
        return
    # Проверка того, что все доп. поля заполнены
    elif combobox_method.current() == 0 and k.get() == "":
        print_error()
        return
    elif combobox_method.current() == 1 and (delta.get() == "" or e.get() == ""):
        print_error()
        return
    elif combobox_method.current() == 2 and e.get() == "":
        print_error()
        return
    elif combobox_method.current() == 3 and k.get() == "":
        print_error()
        return
    # Проверка того, что введенная функция корректна
    else:
        try:
            x = sp.symbols('x')
            funktion = sp.parse_expr(funk.get())
            float(funktion.subs(x, x_min.get()))
        except:
            messagebox.showerror("Ошибка", "Функция введена некорректно")
            return
    global file_name
    file_name = fd.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_name == "":
        return
    # Открываем файл для записи, предварительно очистив его
    f = open(file_name, 'w', encoding='utf-8')
    f.write("y(x) = " + funk.get() + "\nXmin = " + x_min.get() + "\nXmax = " + x_max.get())
    if combobox_method.current() == 0:
        f.write("\nMethod = Монте-Карло\nk = " + k.get())
    elif combobox_method.current() == 1:
        f.write("\nMethod = Дихотомии\ndelta = " + delta.get() + "\ne = " + e.get())
    elif combobox_method.current() == 2:
        f.write("\nMethod = Золотого сечения\ne = " + e.get())
    elif combobox_method.current() == 3:
        f.write("\nMethod = Фибоначчи\nk = " + k.get())


# Функция записи результата в файла
def write_resultfile():
    # Перерасчет значений
    clicked()
    # Запись данных
    write_datafile()
    if file_name == "":
        return
    # Открытие файла на запись (без предварительной очистки)
    f = open(file_name, 'a', encoding='utf-8')
    # Запись результата
    f.write("\n\n" + result.get("1.0", END))


# Объявляем глобальную переменную для использования в write_resultfile()
file_name = ""
# Объявляем глобальную переменную для округления значений
coma = 3

window = Tk()  # Объявление окна
window.title("Приложение для решения одномерных оптимизационных задач")  # Задание титула
# Параметры расположения окна
position_width = int(window.winfo_screenwidth() / 2 - 400)
position_height = int(window.winfo_screenheight() / 2 - 225)
window.geometry('800x450+' + str(position_width) + '+' + str(position_height))  # Задание размеров и расположения окна
# Функции для проверки введенных полей
vcmd_pos_float = (window.register(validate_pos_float), '%P')
vcmd_all_float = (window.register(validate_all_float), '%P')
vcmd_int_positive = (window.register(validate_int_positive), '%P')

# Объявление и расположение Label-ов
Label(window, text="Введите исходные данные:").grid(column=0, row=0)
Label(window, text="y(x) =").grid(column=0, row=1, sticky=E)
Label(window, text="Xmin =").grid(column=0, row=2, sticky=E)
Label(window, text="Xmax =").grid(column=0, row=3, sticky=E)

# Объявление, расположение, параметризация полей
funk = Entry(window, validate='key', width=20)
funk.grid(column=1, row=1)
# Устанавливаем курсор на первое поле
funk.focus()
x_min = Entry(window, validate='key', validatecommand=vcmd_all_float, invalidcommand=print_all_float_error,
              width=10)
x_min.grid(column=1, row=2, sticky=W)
x_max = Entry(window, validate='key', validatecommand=vcmd_all_float, invalidcommand=print_all_float_error,
              width=10)
x_max.grid(column=1, row=3, sticky=W)

# Доп. Label для создания пространства между элементами
Label(window, text="\t").grid(column=2, row=1)
Label(window, text="Выберите метод").grid(column=3, row=1)
# Выпадающий список с методами
combobox_method = Combobox(window, values=("Монте-Карло", "Дихотомии", "Золотого сечения", "Фибоначчи"),
                           state="readonly")
combobox_method.grid(column=3, row=2)
# выполнение selected() при изменении значения
combobox_method.bind("<<ComboboxSelected>>", selected)

# Объявление и расположение доп. Label-ов и полей для каждого метода
lbl_e = Label(window, text="\u03B5 =")
lbl_delta = Label(window, text="\u0394 =")
lbl_k = Label(window, text="k =")
delta = Entry(window, validate='key', validatecommand=vcmd_pos_float, invalidcommand=print_pos_float_error, width=10)
e = Entry(window, validate='key', validatecommand=vcmd_pos_float, invalidcommand=print_pos_float_error, width=10)
k = Entry(window, validate='key', validatecommand=vcmd_int_positive, invalidcommand=print_positive_error, width=10)
temp_elements = [lbl_k, lbl_e, lbl_delta, e, k, delta]

Label(window, text="\t").grid(column=4, row=1)
# Объявление и расположение кнопок; задание функции, которая будет выполняться при нажатии на кнопку
btn_result = Button(window, text="Рассчитать", command=clicked, width=22)
btn_result.grid(column=5, row=1)
btn_enter_data = Button(window, text="Загрузка данных из файла", command=read_datafile, width=22)
btn_enter_data.grid(column=5, row=2)
btn_write_data = Button(window, text="Запись данных в файл", command=write_datafile, width=22)
btn_write_data.grid(column=5, row=3)
btn_write_result = Button(window, text="Запись результатов в файл", command=write_resultfile, width=22)
btn_write_result.grid(column=5, row=4)

# Объявление и расположение текстового поля результата
result = scrolledtext.ScrolledText(window, width=90, height=18, font=("Arial", 11, "normal"), state=DISABLED, wrap=WORD)
result.place(x=5, y=140)


def window_form():
    # Отображение всех компонентов
    mainloop()
