def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def alternate_sort(arr):
    bubble_sort(arr)

    small_pointer, large_pointer = 0, len(arr) - 1
    
    result = []
    while small_pointer < large_pointer:
        result.append(arr[small_pointer])
        result.append(arr[large_pointer])
        small_pointer += 1
        large_pointer -= 1

    # If there is an odd number of elements, add the middle element
    if small_pointer == large_pointer:
        result.append(arr[small_pointer])

    return result

input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
output_array = alternate_sort(input_array)
print(output_array)