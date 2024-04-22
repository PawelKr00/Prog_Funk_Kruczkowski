from functools import reduce

list1 = [1,2,3,4,5,6,7,8]

print(reduce(lambda a, b: a if a > b else b, list1))

def averageOfList(lista):
    sum = reduce(lambda a, b: a+b, lista)
    return sum / len(lista)

print(averageOfList(list1))