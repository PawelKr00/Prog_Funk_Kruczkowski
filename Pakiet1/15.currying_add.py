def curry(x):
    def add(y):
        return x + y
    return add

print(curry(5)(8))