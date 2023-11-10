def find_triplets(arr, target_sum):
    arr.sort()

    triplets = []

    for i in range(len(arr) - 2):
        left_pointer = i + 1
        right_pointer = len(arr) - 1

        while left_pointer < right_pointer:
            current_sum = arr[i] + arr[left_pointer] + arr[right_pointer]

            if current_sum == target_sum:
                triplets.append([arr[i], arr[left_pointer], arr[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
            elif current_sum < target_sum:
                left_pointer += 1
            else:
                right_pointer -= 1

    return triplets

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 15
result = find_triplets(arr, target_sum)
print(result)