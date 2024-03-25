from itertools import product

listA = ['A', 'B', 'C']
listB = ['A', 'B', 'C']

listC = list(product(listA, listB))
print(listC)