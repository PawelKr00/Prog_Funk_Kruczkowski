def describe_structure(data):
    match data:
        case tuple():
            return f'Tupla z {len(data)} elementami'
        case list():
            return f'Lista z {len(data)} elementami'
        

print(describe_structure((3, 6)))
print(describe_structure([3, 6]))
print(describe_structure((3, 6, 12)))
print(describe_structure((3, 6, 5, 7)))
print(describe_structure([3, 6, 99]))
print(describe_structure([3, 6, 99, 19]))
print(describe_structure([3]))