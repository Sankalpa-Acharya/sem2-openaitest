class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)

    def __mul__(self, other):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

    def transpose(self):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[j][i] = self.matrix[i][j]
        return Matrix(result)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(a + b)
print(a * b)
print(a.transpose())
