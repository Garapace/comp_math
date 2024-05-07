"""  Сортировки: пузырьковая, быстрая, подсчётом  """


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def quick_sort(array):
    if len(array) > 1:
        pivot = array[len(array) // 2]             # определяем опорный элемент,
        less = [u for u in array if u < pivot]     # массив с элементами меньше опорного
        equal = [u for u in array if u == pivot]   # массив с элементами равными опорному
        more = [u for u in array if u > pivot]     # массив с элементами больше опорного
        # элементы < и > будут раскладываться пока массив не будет отсортирован
        array = quick_sort(less) + equal + quick_sort(more)
    return array


def count_sort(array):
    count = [0] * (max(array) - min(array) + 1)  # массив подсчёта встречающихся элементов

    for num in array:                            # подсчёт встречающихся элементов
        count[num - min(array)] += 1

    restored_array = []                          # восстанавливаем массив с помощью досчитанных значений
    for i, num in enumerate(count):
        restored_array.extend([i + min(array)] * num)
    return  restored_array


def main():
    array = [7, 1, 15, 90, 5, 3, 71, 23, 15, 40] # начальный массив для сортировки

    print(f"неотсортированный массив:\t{array}")
    print(f"пузырьковая сортировка:\t\t{bubble_sort(array)}")
    print(f"быстрая сортировка:\t\t\t{quick_sort(array)}")
    print(f"сортировка суммированием:\t{count_sort(array)}")


if __name__ == "__main__":
    main()
