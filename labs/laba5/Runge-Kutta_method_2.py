import numpy as np
from matplotlib import pyplot as plt

""" Решение дифференциальных уравнений: Метода Рунге-Кутты 2-го порядка 
=============== Список литературы ===============
1. https://ru.wikipedia.org/wiki/Метод_Рунге_—_Кутты
2. https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FElnF7HEgAl4z%2FmMITO%2BeDH%2FMcPblSzaO9pX5T%2FQ4vMGj6%2F
oxqAT7iGQGAE%2BpTTWQq%2FJ6bpmRyOJonT3VoXnDag%3D%3D%3A%2FБояршинов%20МГ%2C%202008%20--%20Методы%20Выч.Мат.%20(noЭО%2C%20O
CR%2C%20это%20Численные%20Методы%20ч1%2C2%2C3%20под%20одной%20обложкой).pdf&name=Бояршинов%20МГ%2C%202008%20--%20Методы
%20Выч.Мат.%20(noЭО%2C%20OCR%2C%20это%20Численные%20Методы%20ч1%2C2%2C3%20под%20одной%20обложкой).pdf
--> глава 8, страница 172, 185
=============== Начальные условия ===============
     x'' + x = sin(t); x(0) = 0; x'(0) = 0
"""


def f(x, v, t):
    """
        Уравнение разложили на систему
        x` = v
        v` = t - x
    """
    dx_dt = v
    dv_dt = np.sin(t) - x
    return dx_dt, dv_dt


def runge_method(f, conditions, step, step_quantity):
    """
    =============== входные данные ===============
    f             - функция, описывающая уравнение
    conditions    - начальные условия
    step          - шаг
    step_quantity - кол-во шагов

    =============== выходные данные ===============
    x_values      - значения x на каждом шаге
    v_values      - значения производной x на каждом шаге
    """
    x_values = np.zeros(step_quantity + 1)
    v_values = np.zeros(step_quantity + 1)

    x_values[0], v_values[0] = conditions

    for i in range(step_quantity):
        x = x_values[i]
        v = v_values[i]
        t = i * step

        k1x, k1v = f(x, v, t)
        k2x, k2v = f(x + step * k1x, v + step * k1v, t + step)

        x_values[i+1] = x + 0.5 * step * (k1x + k2x)
        v_values[i+1] = v + 0.5 * step * (k1v + k2v)

    return x_values, v_values


def analytic_solution(t):
    return 0.5 * np.sin(t) - 0.5 * t * np.cos(t)


def main():
    condition = [0, 0]
    step = 0.1
    step_quantity = 100

    x_values, v_values = runge_method(f, condition, step, step_quantity)
    t_values = np.linspace(0, step * step_quantity, step_quantity + 1)
    analytic_values = analytic_solution(t_values)
    error_values = np.abs(x_values - analytic_values)

    # plt.plot(t_values, x_values, label="x(t)")
    # plt.plot(t_values, v_values, label="v(t)")
    # plt.plot(t_values, error_values, label="Погрешность")
    # plt.plot(t_values, analytic_values, label="Оригинальный график")
    # plt.legend()
    # plt.grid()
    # plt.show()

    plt.subplot(2, 2, 1)
    plt.plot(t_values, x_values, label="x(t)")
    plt.legend()
    plt.grid()

    plt.subplot(2, 2, 2)
    plt.plot(t_values, v_values, label="v(t)")
    plt.legend()
    plt.grid()

    plt.subplot(2, 2, 3)
    plt.plot(t_values, error_values, label="Погрешность")
    plt.legend()
    plt.grid()

    plt.subplot(2, 2, 4)
    plt.plot(t_values, analytic_values, label="Оригинальный график")
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()
