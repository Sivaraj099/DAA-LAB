def remove_duplicates(array):
    unique_elements = []
    for i in array:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements
array = [1, 10, 11, 12, 11, 1]
result = remove_duplicates(array)
print(result)