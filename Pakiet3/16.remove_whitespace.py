def remove_whitespace(elems):
    output = []
    for elem in elems:
        output.append(elem.replace(' ', ''))
    return output

print(remove_whitespace(['asd asd asd', 'asdf asds']))