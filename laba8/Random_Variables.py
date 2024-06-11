import random
import numpy as np
import time

"""
Разыгрывание случайной величины
Исследование Random-функции, создать большой массив псевдослучайных чисел, узнать сколько раз повторяются
первые 5 чисел в таком же порядке (псевдопериод), посчитать мат.ожидание, дисперсию.
Сформировать Случайную величину с наперед заданными значениями и их вероятностями (задание дискретной СВ).
=============== Список литературы ===============
1. https://ru.wikipedia.org/wiki/Дисперсия_случайной_величины
"""


def find_repeat_nums(random_nums):
    """
    функция считает, сколько раз в изначальном массиве встречается
    последовательность из первых k элементов этого массива
    """
    k = 5
    find_nums = random_nums[:k]
    count = 0
    for i in range(len(random_nums) - k):
        if random_nums[i:i + k] == find_nums:
            count += 1
    print(f"Первые {k} элементов:\t\t{find_nums}")
    print(f"Количество повторений первых {k} элементов: {count}\n")


def math_expectation_variance_numpy(random_nums):
    # Вычисление математического ожидания и дисперсии с помощью библиотеки numpy
    expectation_numpy = np.mean(random_nums)
    variance_numpy = np.var(random_nums)

    print(f"Математическое ожидание (numpy):\t{expectation_numpy}")
    print(f"Дисперсия (numpy):\t\t\t\t\t{variance_numpy}\n")


def math_expectation(random_nums, n):
    # Вычисление математического ожидания
    unique_values, counts = np.unique(random_nums, return_counts=True)
    math_expectation = 0
    for i in range(len(unique_values)):
        math_expectation += unique_values[i] * counts[i] / n
    print(f"Математическое ожидание:\t\t\t{math_expectation}")

    math_expectation_avg = 0
    for i in range(len(random_nums)):
        math_expectation_avg += random_nums[i]
    math_expectation_avg /= n
    print(f"Математическое ожидание (среднее):\t{math_expectation_avg}\n")


def variance(random_nums, n):
    # Вычисление дисперсии
    avg_sum = 0
    for i in random_nums:
        avg_sum += i
    avg_sum /= n

    variance = 0
    for i in range(len(random_nums)):
        variance += (random_nums[i] - avg_sum) ** 2
    variance /= n
    print(f"Дисперсия:\t\t\t\t\t\t\t{variance}\n")


def discrete_random_variable(n):
    # Создание дискретной случайной величины с заданными значениями и вероятностями
    numbers = [i for i in range(0, 10)]
    chance = [0.1 for i in range(0, 10)]

    # Генерация случайной величины с использованием заданных значений и вероятностей
    discrete_variable = np.random.choice(numbers, p=chance)

    print(f"Случайная величина:\t{discrete_variable}")

    # Вычисление вероятностей для каждого значения дискретной случайной величины
    random_nums = np.random.choice(numbers, size=n, p=chance)
    unique_values, counts = np.unique(random_nums, return_counts=True)

    print("Вероятности для каждого значения дискретной случайной величины:")
    for i in range(len(unique_values)):
        print(f"Значение:\t{unique_values[i]}\t|\tВероятность:\t{counts[i] / n}")

    sum_of_all_values = 0
    for i in range(len(unique_values)):
        sum_of_all_values += counts[i] / n
    print(f"\nСумма вероятностей всех значений:\t{sum_of_all_values}")


def main():
    #  инициализация случайных величин
    random.seed(time.time())
    n = 1000000
    random_nums = [random.randint(0, 9) for i in range(n)]

    find_repeat_nums(random_nums)
    math_expectation_variance_numpy(random_nums)
    math_expectation(random_nums, n)
    variance(random_nums, n)

    discrete_random_variable(n)


if __name__ == "__main__":
    main()
