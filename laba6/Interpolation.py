import numpy as np
from matplotlib import pyplot as plt

""" Интерполяция: многочлен Лагранжа
=============== Список литературы ===============
1. https://ru.wikipedia.org/wiki/Интерполяционный_многочлен_Лагранжа
2. https://www.youtube.com/watch?v=nj2RBZ6xFeY
3. https://goo.su/4skJFSh --> глава 1, страница 42
=============== Начальные условия ================
              y = |x|, x ∈ [-2; 2]
"""


def method_lagrange(x_values, y_values, x):
    """
    :param x_values:  - начальные данные для x
    :param y_values:  - начальные данные для y
    :param x:         - точка, для которой необходимо найти соответсвующий y
    :return:          - результат вычислений методом Лагранжа
    """
    result = 0
    for i in range(len(x_values)):  # реализация метода Лагранжа
        li_x = y_values[i]
        for j in range(len(x_values)):
            if i != j:
                li_x *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += li_x
    return result


def main():
    x = 3      # x для примера
    steps = 7  # кол-во точек для графика
    a = 2
    b = -2

    x_values = np.linspace(-2, 2, steps)
    ch_values = [(b + a) / 2 + ((b - a) / 2) * np.cos(((2 * i + 1) / (2 * (steps + 1))) * np.pi)
                 for i in range(steps)]       # значения функции по оси ординат
    y_values = np.abs(ch_values)              # значения функции по оси абсцисс

    print(f"x = {x_values}\ny = {y_values}")
    print(f"при x = {x} y = {np.round(method_lagrange(x_values, y_values, x), 2)}")

    x_i_values = np.linspace(-2, 2, 200)
    y_i_values = method_lagrange(ch_values, y_values, x_i_values)

    plt.plot(x_values, np.abs(x_values), label="y = |x|")                 # вывод оригинального графика
    plt.plot(x_i_values, y_i_values, label="Интерполяция Лагранжа")           # график через метод Лагранжа
    plt.scatter(ch_values, y_values, color="black", label="Начальные данные")  # точки для метода Лагранжа
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
