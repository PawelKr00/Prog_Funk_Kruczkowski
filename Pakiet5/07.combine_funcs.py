def compose(a, b):
    return lambda x: a(b(x))

def func1(x):
    return x * x

def func2(x):
    return x + 5

print(compose(func1, func2)(5))