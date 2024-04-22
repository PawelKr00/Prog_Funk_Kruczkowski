def sum_dicts(*args):
    final_dict = {}
    for arg in args:
        for key, value in arg.items():
            if key not in final_dict:
                final_dict[key] = value
            else:
                final_dict[key] += value
    return final_dict

print(sum_dicts({'a': 1, 'b': 1, 'c': 1}, {'b': 1, 'c': 1, 'd': 1}, {'c': 1, 'd': 1, 'e': 1}))