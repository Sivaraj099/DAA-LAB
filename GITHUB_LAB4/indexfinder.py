def find_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

input_array = [4, 2, 7, 1, 2, 6, 2, 8, 2]
target_number = 2
result = find_indices(input_array, target_number)

print(f"The indices of {target_number} in the array are: {result}")
