def evens(lista):
    newList = []
    for i in lista:
        if i%2==0:
            newList.append(i)
    return newList

print(evens([1,2,3,4,5,6,7,8,9]))

areaOfRectangel = lambda a,b: a*b
print(areaOfRectangel(2,6))