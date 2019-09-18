# -1,-3,-2
# -1,0,-2,2
# 0,-2,0
# 1
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(3^4^3)
max_sub,fn = nums[0],0
for i in nums:
    fn = max([i,fn+i])
    # print("fn",fn)
    max_sub = max(max_sub,fn)
    print("max_sub",max_sub)
# right = len(nums)
# left = 0
# sumr = 0
# suml = 0
# i = 0
# for i in range(right):
#     if sum(nums[:i+1]) < suml:
#         suml = sum(nums[:i+1])
#         left = i+1
#     if sum(nums[-i-1:]) < sumr:
#         sumr = sum(nums[-i-1:])
#         right = -i-1
# if (i+1) * 2 < len(nums) and nums[i+1] < 0:
#     if sum(nums[-i-2:]) < sumr and sum(nums[-i-2:]) <= sum(nums[:i+2]):
#         sumr = sum(nums[-i-2:])
#         right = -i-2
#     elif sum(nums[:i+2]) < suml and sum(nums[-i-2:]) >= sum(nums[:i+2]):
#         suml = sum(nums[:i+2])
#         left = i+2
# if nums[left:right] == []:
#     print("a", max(nums))
# else:
#     print("b", sum(nums[left:right]))
# print(nums[left:right])
