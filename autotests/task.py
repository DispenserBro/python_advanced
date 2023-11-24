import numpy as np

class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __repr__(self) -> str:
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self) -> str:
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __eq__(self, other: 'Matrix') -> bool:
        if self.rows != other.rows or self.cols != other.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False

        return True
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            return
        
        new_matrix = Matrix(self.rows, self.cols)
        
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.data[i][j] = self.data[i][j] + other.data[i][j]
        return new_matrix

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            return

        new_matrix = Matrix(other.rows, self.cols)
        result = np.matrix(self.data) * np.matrix(other.data)
        new_matrix.data = result.tolist()
        return new_matrix

# Создаем матрицы
matrix1 = Matrix(2, 3)

matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)