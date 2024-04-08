def count_unique_elements(elems):
    output = 0
    for elem in elems:
        if elems.count(elem) == 1:
            output += 1
    return output

print(count_unique_elements([1,2,3,3,4,5,6,6,7,8,9,9]))