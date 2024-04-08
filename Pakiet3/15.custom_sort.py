def custom_sort(elems, key):
    return sorted(elems, key=key)

print(custom_sort([1,2,3,4,5,6,7,8,9], lambda x: x%2 == 0))