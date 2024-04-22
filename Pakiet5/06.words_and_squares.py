def words_starting_with_a(lista):
    newList = []
    for i in lista:
        if list(i)[0] in ['a', 'A']:
            newList.append(i)
    return newList

print(words_starting_with_a(['avcss', 'asdd', 'vsdss', 'sdfsdfs', 'Adsafasf']))


def power_up(x):
    return x * x

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = list(map(power_up, numbers))

print(numbers)