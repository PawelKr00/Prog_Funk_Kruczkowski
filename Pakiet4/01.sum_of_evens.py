def sum_evens(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum

print(sum_evens([1,2,3,4,5,6,7,8,9]))