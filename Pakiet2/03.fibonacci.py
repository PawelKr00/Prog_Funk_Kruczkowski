def fibonacci():
    n = 1
    m = 1
    while True:
        yield n
        k = n
        n = m
        m = k + m

generator = fibonacci()
for _ in range(10):
    print(next(generator))