"""Численное интегрирование"""
"""
----------------- Список литературы -----------------
1. https://ru.wikipedia.org/wiki/Численное_интегрирование
2. https://ru.wikipedia.org/wiki/Формула_Симпсона#Составная_формула_(формула_Котеса)
3. https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FElnF7HEgAl4z%2FmMITO%2BeDH%2FMcPblSzaO9pX5T%2FQ4vMGj6%2
FoxqAT7iGQGAE%2BpTTWQq%2FJ6bpmRyOJonT3VoXnDag%3D%3D%3A%2FБояршинов%20МГ%2C%202008%20--%20Методы%20Выч.Мат.%20
(noЭО%2C%20OCR%2C%20это%20Численные%20Методы%20ч1%2C2%2C3%20под%20одной%20обложкой).pdf&name=Бояршинов%20МГ%2C%202008%20--%20
Методы%20Выч.Мат.%20(noЭО%2C%20OCR%2C%20это%20Численные%20Методы%20ч1%2C2%2C3%20под%20одной%20обложкой).pdf
----> глава 7, страница 139
"""

import math
import numpy as np
from matplotlib import pyplot as plt


def f(x):  # функция
    return math.sin(x)


def method_rectangle(n, a, b):    # метод прямоугольников
    result = 0
    h = (b - a) / n               # шаг сетки
    x = a + h                     # точка в которой вычисляется интеграл

    for i in range(1, n):         # реализация метода прямоугольников
        result += f(x - h / 2)
        x += h
    return h * result


def method_trapezoid(n, a, b):    # метод трапеций
    result = 0
    h = (b - a) / n
    x = a + h
    for i in range(1, n-1):
        result += f(x)
        x += h
    return h * ((f(a) + f(b)) / 2 + result)


def method_kotes(n, a, b):  # метод Котеса
    result = 0
    h = (b - a) / n
    x = a + h
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)
        x += h
    return (h / 3) * (f(a) + result + f(b))


def main():
    # начальные значения
    start = 0
    end = math.pi
    steps = 1000  # кол-во отрезков, шагов

    print(f'Метод прямоугольников:\t{method_rectangle(steps, start, end)}')
    print(f'Метод трапеций:\t\t\t{method_trapezoid(steps, start, end)}')
    print(f'Метод Котеса:\t\t\t{method_kotes(steps, start, end)}')

    # правильные координаты
    x = np.linspace(0, 2 * end, steps)
    y = []
    for i in x:
        y.append(1 - math.cos(i))

    # погрешность различными методами
    y_rectangle = []
    y_trapezoid = []
    y_kotes = []
    for i in x:
        y_rectangle.append(method_rectangle(steps, 0, i) - (1 - math.cos(i)))
        y_trapezoid.append(method_trapezoid(steps, 0, i) - (1 - math.cos(i)))
        y_kotes.append(method_kotes(steps, 0, i) - (1 - math.cos(i)))

    # построение графиков
    # позволяет вывести несколько графиков в одном окне subplot(2 - строки, 2 - столбцы, 1 - индекс позиции графика)
    plt.subplot(2, 2, 1)
    plt.plot(x, y_rectangle, label="Погрешность методом прямоугольников")   # размещение графика
    plt.xlabel('axis x')                                                          # подпись оси абсцисс
    plt.ylabel('axis y')                                                          # подпись оси ординат
    plt.legend()                                                                  # вывод легенды (название графика)
    plt.grid()                                                                    # сетка в графике

    plt.subplot(2, 2, 2)
    plt.plot(x, y_trapezoid, label="Погрешность методом трапеций")
    plt.xlabel('axis x')
    plt.ylabel('axis y')
    plt.legend()
    plt.grid()

    plt.subplot(2, 2, 3)
    plt.plot(x, y_kotes, label="Погрешность методом Котеса")
    plt.xlabel('axis x')
    plt.ylabel('axis y')
    plt.legend()
    plt.grid()

    plt.subplot(2, 2, 4)
    plt.plot(x, y, label="Оригинальный график sin(x)")
    plt.xlabel('axis x')
    plt.ylabel('axis y')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
