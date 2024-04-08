def sum_of_squares_of_odds(nums):
    sum = 0
    for num in nums:
        if num % 2 == 1:
            sum += num * num
    return sum

print(sum_of_squares_of_odds([1,2,3,4,5,6,7,8,9]))