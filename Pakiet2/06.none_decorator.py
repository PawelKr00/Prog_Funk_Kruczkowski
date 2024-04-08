def none_decorator(func):
    def check_for_zero(a, b):
        if b == 0:
            return None
        return func(a, b)
    return check_for_zero

def divide_numbers(a, b):
    return a / b

divide_numbers = none_decorator(divide_numbers)

print(divide_numbers(6,0))