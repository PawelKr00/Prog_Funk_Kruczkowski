from functools import partial

def multiply(x, y):
    return x * y

part3 = partial(multiply, 3)

print(part3(11))