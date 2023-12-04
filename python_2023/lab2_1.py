import numpy as np

# початкова матриця
matrix = np.array([[1, 2, 3],
                    [9, 6, 3],
                    [1, 4, 2]])

# Знаходимо суми стовпців
column_sums = np.sum(matrix, axis=0)

# Створюємо список пар (сума, номер стовпця)
sum_column_pairs = [(column_sums[i], i) for i in range(len(column_sums))]

# Впорядковуємо список за сумами в незростаючому порядку
sorted_sum_column_pairs = sorted(sum_column_pairs, key=lambda x: x[0], reverse=True)

# Створюємо нову матрицю зі стовпцями впорядкованими за сумами (у зворотньому порядку)
sorted_matrix = matrix[:, [pair[1] for pair in sorted_sum_column_pairs]]

print("Матриця зі стовпцями впорядкованими за сумами (у зворотньому порядку):")
print(sorted_matrix)
