def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

print(filter_even_numbers([2,5,7,5,4,3,7,8,6,2]))