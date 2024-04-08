def rotate_list(elems, steps):
    output = []
    for i in range(steps, 0, -1):
        output.append(elems[len(elems)-i])
    for i in range(len(elems) - steps):
        output.append(elems[i])
    return output

print(rotate_list([1,2,3,4,5,6,7,8,9], 4))