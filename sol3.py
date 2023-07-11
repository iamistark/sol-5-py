def sorted_squares(nums):
    squared_nums = [num ** 2 for num in nums]
    squared_nums.sort()
    return squared_nums
#Driver code
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)
