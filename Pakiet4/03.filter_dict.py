def filter_dict(dict):
    new_dict = {}
    for key, value in dict.items():
        if value % 2 == 0:
            new_dict[key] = value
    return new_dict

print(filter_dict({'abc': 2, 'def': 3, 'grd': 4}))