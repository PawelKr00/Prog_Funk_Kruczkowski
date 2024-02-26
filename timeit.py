import time

def timeit(x):
    seconds = time.thread_time()
    def exponent(y):
        return 5 ** y
    answer = exponent(x)
    seconds2 = time.thread_time()
    return seconds2 - seconds


print(timeit(10000000))

