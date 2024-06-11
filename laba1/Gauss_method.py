def gauss_method(matrix, vector):
    n = len(matrix)
    for col in range(n):
        # поиск строки с максимальным коэффициент
        max_row = col
        # проходим по всем строкам матрицы коэфициэнтов и находим максимальную строку
        for row in range(col + 1, n):
            if abs(matrix[row][col] > abs(matrix[max_row][col])):
                max_row = row

        # меняем местами текущую строку и максимальную
        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
        vector[col], vector[max_row] = vector[max_row], vector[col]

        # идём по строкам матрицы, где нужно занулить элементы
        for row in range(col + 1, n):
            # записываем коэффициент на который нужно домножить число в максимальной строке, чтобы получить нуль в текущей
            coef = - matrix[row][col] / matrix[col][col]
            # идём по столбцам матрицы
            for colum in range(col, n):
                # если начальный и текущий столбец равны, то элемент зануляем
                if col == colum:
                    matrix[row][colum] = 0
                # если столбцы не равны, тогда мы вычитаем из следующего элемента элемент над ним домноженынй на коэффициент
                else:
                    matrix[row][colum] += coef * matrix[col][colum]
            # делаем то же самое с векторами
            vector[row] += coef * vector[col]

    # обратный ход
    x = [0 for x in range(n)]
    for col in range(n - 1, -1, -1):
        x[col] = vector[col] / matrix[col][col]
        for row in range(col - 1, -1, -1):
            vector[row] -= matrix[row][col] * x[col]
    return x


def main():
    # вводим матрицу коэффициэнтов
    matrix = [[3, 2, -5],
              [2, -1, 3],
              [1, 2, -1]]

    # вводим искомый вектор
    vector = [-1, 13, 9]

    print(f"Решение системы уравнений:\n{gauss_method(matrix, vector)}")


if __name__ == "__main__":
    main()