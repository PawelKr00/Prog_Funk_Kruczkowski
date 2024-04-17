import math
def divide(elems, size):
    output = []
    for i in range(math.ceil(len(elems) / size)):
        output.append(elems[i * size:(i + 1) * size])
    return output


print(divide([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))