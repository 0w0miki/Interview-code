nums = [1]
val = 1
length = 0
l = len(nums)
i = 0
while val in nums:
    if nums[i] == val:
        length += 1
        nums.pop(i)
        print(nums)
    else:
        i += 1
print(length)
print(nums)
