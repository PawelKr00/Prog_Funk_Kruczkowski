def flatten_list(l):
    output = []
    for n in l:
        if type(n) == list:
            output += flatten_list(n)
        else:
            output.append(n)
    return output

print(flatten_list([1,2,3,[4,5,[6,7], [8,9]]]))