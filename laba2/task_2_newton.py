""" функция уравнения f(x) = x^2 - 2.
    вычисляет значение функции f(x) = x^2 - 2."""
def f(x):
    return x**2 - 2


""" производная функции уравнения f(x) = x^2 - 2. используется в методе Ньютона
    вычисляет значение производной f'(x) = 2x """
def f_deriv(x):
    return 2*x


def newton_method(f, f_derive, x0, delta):
    while True:
        x1 = x0 - f(x0) / f_derive(x0) # формула метода ньютона
        if abs(x1 - x0) < delta: # если разность меньше погрешности, то выходим из цикла
            break
        x0 = x1
    return x1 # возвращается приближенное значение корня


def newton_method_print_root():
    print(f"найденный положительный корень методом ньютона - {newton_method(f, f_deriv, x0_positive, delta)}")
    print(f"найденный отрицательный корень методом ньютона - {newton_method(f, f_deriv, x0_negative, delta)}")
    print()


x0_positive, x0_negative = 1.5, -1.5
delta = 1e-6