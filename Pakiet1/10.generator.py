def even_generator():
    n = 0
    while True:
        yield n
        n += 2

generator = even_generator()
even_nums = [next(generator) for _ in range(10)]
print(even_nums)