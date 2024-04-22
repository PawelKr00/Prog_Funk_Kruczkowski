global_variable = 10

def function_with_global_variable(x):
    return x + global_variable

def function_with_local_variable(x):
    local_variable = 5
    return x * local_variable

print(function_with_global_variable(5))
print(function_with_local_variable(5))