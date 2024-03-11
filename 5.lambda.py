power_up = lambda x: x ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(numbers)):
    numbers[i] = power_up(numbers[i])

print(numbers)