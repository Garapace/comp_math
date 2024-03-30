from math import sin, cos, pi
from matplotlib import pyplot as plt


def final_difference(f, x, h=1e-5):  # f - функция, x - точка, в которой считается производная, h - шаг разности
    # числитель - конечная разность функции, знаменатель - шаг разности
    return (f(x + h) - f(x - h)) / (2 * h)


def final_difference_right(f, x, h=1e-8):  # f - функция, x - точка, в которой считается производная, h - шаг разности
    # числитель - конечная разность функции, знаменатель - шаг разности
    return (f(x + h) - f(x)) / h


def f_deriv(x):  # производная функции
    return cos(x)


def f(x):  # начальная функция
    return sin(x)


def main():
    x = []  # массив точек
    original_y = []  # массив точек оригинальной производной
    fin_diff_y = []  # массив точек вычисленной производной
    y_diff = []  # список разности массивов оригинальной и вычисленной производных

    for i in range(0, 10 * int(4 * pi), 1):  # заполнение массивов
        x.append(i / 10)
        original_y.append(f_deriv(i / 10))
        fin_diff_y.append(final_difference_right(f, i / 10))
        y_diff.append(original_y[i] - fin_diff_y[i])

    plt.plot(x, y_diff, label="Разность производных")  # построение графика
    plt.xlabel = "x"  # подписи осей
    plt.ylabel = "y"
    plt.title("График кривых")  # название кривой
    plt.legend()  # вывод легенды
    plt.show()  # вывод окна с графиком


if __name__ == "__main__":
    main()
