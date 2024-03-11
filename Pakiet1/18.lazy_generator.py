def lazy_gen():
    n = 1
    while True:
        yield n**5
        n += 1

generator = lazy_gen()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))