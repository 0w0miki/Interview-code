nums = [1,1,2]
print(id(nums))
def removeDuplicates(nums):
    nums = list(set(nums))
    print(id(nums))
    return len(nums)
removeDuplicates(nums)
