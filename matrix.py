import numpy as np

def main():
    try:
        n = int(input("Введите количество строк N: "))
        m = int(input("Введите количество столбцов M: "))
    except ValueError:
        print("Ошибка ввода. Введите целые числа.")
        return

    if n <= 0 or m <= 0:
        print("Размеры матрицы должны быть положительными.")
        return

    matrix = np.random.randint(1, 11, size=(n, m))
    
    print("Исходная матрица:")
    print(matrix)

    transposed_matrix = matrix.T
    print("Транспонированная матрица:")
    print(transposed_matrix)
    
    # Определитель можно найти только если матрица квадратная, т.е. N == M
    if n == m:
        det_original = np.linalg.det(matrix)
        det_transposed = np.linalg.det(transposed_matrix)
        
        print("Определитель исходной матрицы:", det_original)
        print("Определитель транспонированной матрицы:", det_transposed)
        
        if np.isclose(det_original, det_transposed):
            print("Результат сравнения: Определители равны.")
        else:
            print("\nРезультат сравнения: Определители не равны.")
    else:
        print("Невозможно вычислить определитель: матрица не является квадратной.")


main()