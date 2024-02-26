def make_multiplier(x):

    def multiplier(y):
        return x * y

    return multiplier

double = make_multiplier(4)

print(double(6))