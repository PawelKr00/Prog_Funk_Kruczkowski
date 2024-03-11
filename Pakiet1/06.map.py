def power_up(x):
    return x * x

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = list(map(power_up, numbers))

print(numbers)