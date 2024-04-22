def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

fibonacci = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci), end=" ")

print()

file_reader = read_large_file("large_file.txt")
for line in file_reader:
    print(line)