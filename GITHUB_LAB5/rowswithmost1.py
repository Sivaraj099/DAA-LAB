def find_row_with_most_ones(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    max_ones_row = 0  # Initialize the row with the most 1s
    max_ones_count = matrix[0].count(1)  # Count of 1s in the first row

    for i in range(1, rows):
        # Count the number of 1s in the current row
        current_ones_count = matrix[i].count(1)

        # Update if the current row has more 1s
        if current_ones_count > max_ones_count:
            max_ones_count = current_ones_count
            max_ones_row = i

    return max_ones_row

binary_matrix = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1]
]

result = find_row_with_most_ones(binary_matrix)
print(f"The row with the most 1s is row {result}")
