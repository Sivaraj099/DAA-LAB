def max_subarray_sum(arr):
    if not arr:
        return 0, []

    max_sum = arr[0]
    current_sum = 0
    start_index = 0
    end_index = 0
    current_start_index = 0

    for i, num in enumerate(arr):
        if num > current_sum + num:
            current_sum = num
            current_start_index = i
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = current_start_index
            end_index = i

    return max_sum, arr[start_index:end_index + 1]

input_array = [12, 3, 4, 1, 6, 9]
result_sum, result_elements = max_subarray_sum(input_array)
print(f"Maximum Subarray Sum: {result_sum}")
print(f"Maximum Subarray Elements: {result_elements}")
