""" функция уравнения f(x) = x^2 - 2.
    вычисляет значение функции f(x) = x^2 - 2."""


def f(x):
    return x ** 2 - 2


def simple_iteration(phi, x0, delta, max_iter=1000):
    '''функция phi должна обеспечивать сходимость'''
    for i in range(max_iter):
        x1 = phi(x0)  # вычисление приближения к корню
        if abs(x1 - x0) < delta:
            return x1
        x0 = x1
    print("выход за пределы кол-ва итераций")
    return x0  # возвращаем последнее ближайшее к корню значение


def simple_iteration_print_root():
    print(f"найденный положительный корень методом простых итераций - {simple_iteration(phi, x0_positive, delta)}")
    print(f"найденный отрицательный корень методом простых итераций - {simple_iteration(phi, x0_negative, delta)}")
    print()


phi = lambda x: (x + 2 / x) / 2  # здесь фи уже посчитана и находится в той форме, в которой должна быть для решения конкретно этого уравнения
x0_positive, x0_negative = 0.1, -2
delta = 1e-6