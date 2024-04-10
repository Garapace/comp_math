import numpy as np
from matplotlib import pyplot as plt

""" Решение дифференциальных уравнений: Метод Эйлера """
"""
=============== Список литературы ===============
1. 
2. 
"""

"""
=============== Начальные условия ===============
    x'' + x = 0; x(0) = 1, x'(0) = 1
"""


def f(x, v):
    """
    уравнение разложили на систему
    x' = v
    v' = -x
    """
    dx_dt = v
    dv_dt = -x
    return dx_dt, dv_dt


def eulers_method(f, conditions, step, step_quantity):
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

    x_values[0] = conditions[0]
    v_values[0] = conditions[1]

    for i in range(step_quantity):
        x = x_values[i]
        v = v_values[i]

        dx_dt, dv_dt = f(x, v)

        x_values[i+1] = x + dx_dt * step
        v_values[i+1] = v + dv_dt * step

    return x_values, v_values


def analitic_solution(t):        # решение при котором C1 = 1 и C2 = 1
    return np.cos(t) + np.sin(t)


def main():
    condition = [1, 1]
    step = 0.1
    step_quantity = 100

    x_values, v_values = eulers_method(f, condition, step, step_quantity)
    t_values = np.linspace(0, step * step_quantity, step_quantity + 1)
    analitic_values = analitic_solution(t_values)
    error_values = np.abs(x_values - analitic_values)

    plt.subplot(3, 1, 1)
    plt.plot(t_values, x_values, label="x(t)")
    plt.legend()
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t_values, v_values, label="v(t)")
    plt.legend()
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t_values, error_values, label="Погрешность")
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()
