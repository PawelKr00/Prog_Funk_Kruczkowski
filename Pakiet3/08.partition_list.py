def partition_list(nums):
    output = [[],[]]
    for num in nums:
        if num % 2 == 0:
            output[0].append(num)
        else:
            output[1].append(num)
    return output

print(partition_list([1,2,3,4,5,6,7,8,9]))
