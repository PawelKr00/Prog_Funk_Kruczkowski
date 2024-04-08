def concat_strings(*args):
    output = ''
    for arg in args:
        output += arg + ' '
    return output


print(concat_strings('abc', 'def', 'ghi'))