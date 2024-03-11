def compose(a, b):
    return lambda x: a(b(x))

def func1(x):
    return x + 'funkcja1'

def func2(x):
    return x + 'funkcja2'

print(compose(func1, func2)('funkcja3'))