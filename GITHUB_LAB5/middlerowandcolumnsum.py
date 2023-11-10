def middle_row_column_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Find the middle row and calculate its sum
    middle_row = rows // 2
    middle_row_sum = sum(matrix[middle_row])

    # Find the middle column and calculate its sum
    middle_col = cols // 2
    middle_col_sum = sum(row[middle_col] for row in matrix)

    return middle_row_sum, middle_col_sum

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sum, col_sum = middle_row_column_sum(matrix)
print(f"Sum of the middle row: {row_sum}")
print(f"Sum of the middle column: {col_sum}")
