def combinations(lista):
    result = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            result.append((lista[i], lista[j]))
    return result

final = combinations([1,2,3,4,5,6])

print(final)