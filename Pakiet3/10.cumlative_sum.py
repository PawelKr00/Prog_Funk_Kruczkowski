def cumlative_sum(nums):
    output = []
    for i in range(len(nums)):
        sum = 0
        for j in range(i+1):
            sum += nums[j]
        output.append(sum)
    return output

print(cumlative_sum([1,2,3,4,5,6,7,8,9]))