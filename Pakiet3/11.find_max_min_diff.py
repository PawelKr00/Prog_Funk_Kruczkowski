def find_max_min_diff(nums):
    max_num = max(nums)
    min_num = min(nums)
    return max_num - min_num

print(find_max_min_diff([1,2,3,4,5,6,7,8,9]))