def recursive_sum(nums):
    sum = 0;
    for num in nums:
        if type(num) == int:
            sum += num
        else:
            sum += recursive_sum(num)
    return sum

print(recursive_sum([12, 323, [12, 23,34, [23,112], [12, 34]]]))