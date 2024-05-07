import numpy as np
from matplotlib import pyplot as plt

""" Интерполяция: многочлен Лагранжа
=============== Список литературы ===============
1. https://ru.wikipedia.org/wiki/Интерполяционный_многочлен_Лагранжа
2. https://www.youtube.com/watch?v=nj2RBZ6xFeY
3. https://goo.su/4skJFSh --> глава 1, страница 42
=============== Начальные условия ===============
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
    for i in range(len(x_values)): # реализация метода Лагранжа
        step = y_values[i]
        for j in range(len(x_values)):
            if i != j:
                step *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += step
    return result


def main():
    x = 3      # x для примера
    steps = 6  # кол-во точек для графика
    x_values = np.linspace(-2, 2, steps)  # значения функции по оси ординат
    y_values = abs(x_values)                    # значения функции по оси абсцисс

    print(f"x = {x_values}\ny = {y_values}")
    print(f"при x = {x} y = {np.round(method_lagrange(x_values, y_values, x), 2)}")

    x_i_values = np.linspace(-2, 2, 101)
    y_i_values = method_lagrange(x_values, y_values, x_i_values)

    plt.plot(x_i_values, np.abs(x_i_values), label="y = |x|")           # вывод оригинального графика
    plt.plot(x_i_values, y_i_values, label="Интерполяция Лагранжа")     # график через метод Лагранжа
    plt.scatter(x_values, y_values, color="black", label="Начальные данные")  # точки для метода Лагранжа
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
