def multiply(x, y):
    result = 0

    if y < 0:
        x, y = -x, -y

    for _ in range(y):
        result += x

    return result

num1 = 5
num2 = 3
result = multiply(num1, num2)

print(f"{num1} * {num2} = {result}")
