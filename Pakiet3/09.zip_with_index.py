def zip_with_index(elems):
    output = []
    for i in range(len(elems)):
        output.append(str(i) + str(elems[i]))
    return output

print(zip_with_index(['a', 'b', 'c', 'd', 'e']))

