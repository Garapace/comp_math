"""Численное интегрирование"""

import math
import numpy
from matplotlib import pyplot


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
    steps = 1000  # кол-во отрезков

    print(f'Метод прямоугольников:\t{method_rectangle(steps, start, end)}')
    print(f'Метод трапеций:\t\t\t{method_trapezoid(steps, start, end)}')
    print(f'Метод Котеса:\t\t\t{method_kotes(steps, start, end)}')

    # правильные координаты
    x = numpy.linspace(0, 2 * end, steps)
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
    # pyplot.plot(x, y, label = "sin(x)")
    pyplot.plot(x, y_rectangle, label="Погрешность методом прямоугольников")
    pyplot.plot(x, y_trapezoid, label="Погрешность методом трапеций")
    pyplot.plot(x, y_kotes, label="Погрешность методом Котеса")
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.legend()
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    main()
