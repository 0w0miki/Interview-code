nums = [1,3,4,5]
target = 6
i,l = 0,len(nums)
# if target not in nums:
#     i = 0 if target<nums[0] else l
# else:
#     while target > nums[i]:
#         i += 1
while i < l and target > nums[i]:
    i += 1
print(i)
