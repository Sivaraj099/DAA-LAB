def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

input_array = [0, 0, 1, 2, 0, 1, 2, 2, 1]

selection_sort(input_array)
print(input_array)