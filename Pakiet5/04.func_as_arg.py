def applyToAll(lista, func):
    newList = []
    for elem in lista:
        newList.append(func(elem))
    return newList


print(applyToAll([1,2,3,4,5,6,7,8,9, 'a'], lambda elem: elem + elem))