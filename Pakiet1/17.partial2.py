from functools import partial

def add(x, y):
    return x + y

add5 = partial(add, 5)

print(add5(7))