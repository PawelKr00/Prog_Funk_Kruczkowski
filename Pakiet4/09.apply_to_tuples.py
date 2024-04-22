def apply_to_tuples(lista):
    afterTuple = []
    for item in lista:
        afterTuple.append((item[0]*2, item[1]*2))
    return afterTuple

print(apply_to_tuples([(1,2),(2,3),(3,4),(4,5)]))