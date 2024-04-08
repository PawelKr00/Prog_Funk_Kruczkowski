def remove_duplicates(elems):
    for i in range(len(elems),1,-1):
        if elems.count(elems[i-1]) > 1:
            del elems[i-1]
    return elems

print(remove_duplicates([1,2,3,4,1,5,6,7,6,8,9]))