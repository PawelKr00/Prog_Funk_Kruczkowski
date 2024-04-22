from itertools import permutations
def all_permutations(lista):
    return list(permutations(lista))

print(all_permutations([1,2,3,4,5]))