def find_most(lista):
    return max(set(lista), key=lista.count)

print(find_most([1,1,1,1,2,2,2,2,2,3,4,5,6]))