def interchange_diagonals(matrix):
    size = len(matrix)
    for i in range(size):
        matrix[i][i], matrix[i][size - 1 - i] = matrix[i][size - 1 - i], matrix[i][i]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

interchange_diagonals(matrix)

print("\nMatrix after Diagonal Interchange:")
for row in matrix:
    print(row)
