def bubble_sort(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    flattened_matrix = [matrix[i][j] for i in range(rows) for j in range(cols)]

    n = rows * cols
    for i in range(n):
        for j in range(0, n - i - 1):
            if flattened_matrix[j] > flattened_matrix[j + 1]:
                flattened_matrix[j], flattened_matrix[j + 1] = flattened_matrix[j + 1], flattened_matrix[j]

    sorted_matrix = [flattened_matrix[i:i+cols] for i in range(0, n, cols)]

    return sorted_matrix

def replace_diagonals_with_zeros(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i][i] = 0

    for i in range(rows):
        matrix[i][cols - 1 - i] = 0
        
matrix = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

sorted_matrix = bubble_sort(matrix)

replace_diagonals_with_zeros(sorted_matrix)

for row in sorted_matrix:
    print(row)
