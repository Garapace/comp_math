import random
from time import time


"""  Сортировки: пузырьковая, быстрая, подсчётом  """

count_bubble = 0
count_quick = 0
count_count = 0


def bubble_sort(array):
    global count_bubble
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                count_bubble += 1
    return array


def quick_sort(array):
    global count_quick
    count_quick += 1
    if len(array) > 1:
        pivot = array[len(array) // 2]             # определяем опорный элемент,
        less = [u for u in array if u < pivot]     # массив с элементами меньше опорного
        equal = [u for u in array if u == pivot]   # массив с элементами равными опорному
        more = [u for u in array if u > pivot]     # массив с элементами больше опорного
        # элементы < и > будут раскладываться пока массив не будет отсортирован
        array = quick_sort(less) + equal + quick_sort(more)
    return array


def count_sort(array):
    global count_count
    count = [0] * (max(array) - min(array) + 1)  # массив подсчёта встречающихся элементов

    for num in array:                            # подсчёт встречающихся элементов
        count[num - min(array)] += 1
        count_count += 1

    restored_array = []                          # восстанавливаем массив с помощью досчитанных значений
    for i, num in enumerate(count):
        restored_array.extend([i + min(array)] * num)
        count_count += num
    return restored_array


def main():
    # array = [7, 1, 15, 90, 5, 3, 71, 23, 15, 40] # начальный массив для сортировки
    array = []
    for i in range(2000):
        array.append(random.randint(-1000, 1000))
    print(f"неотсортированный массив:\t{array}\n")

    start_bubble = time()
    print(f"пузырьковая сортировка:\t\t{bubble_sort(array)}")
    end_bubble = time()
    print(f"время бабл {end_bubble - start_bubble}")
    print(f"итерации бабл - {count_bubble}\n")

    start_quick = time()
    print(f"быстрая сортировка:\t\t\t{quick_sort(array)}")
    end_quick = time()
    print(f"время квик {end_quick - start_quick}")
    print(f"итерации квик - {count_quick}\n")

    start_count = time()
    print(f"сортировка суммированием:\t{count_sort(array)}")
    end_count = time()
    print(f"время подсчёт {end_count - start_count}")
    print(f"итерации подсчёт - {count_count}\n")


if __name__ == "__main__":
    main()
