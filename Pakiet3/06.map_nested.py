def map_nested(elems):
    output = []
    for elem in elems:
        if type(elem) == list:
            output.append(map_nested(elem))
        else:
            output.append(double_elem(elem))
    return output


def double_elem(x):
    return x + x


print(map_nested([12, 23, '45', [12, 'wew'], ['asa', 33, [2, 'a']]]))