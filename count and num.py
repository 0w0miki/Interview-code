# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221
# 13211311123113112211
# 11131221133112132113212221
# 3113112221232112111312211312113211
count = 0
nums = "1"
prenum = ""
n = 6

for i in range(n):
    count = 0
    prenum = ""
    digit = nums[0]
    for j in range(len(nums)):
        if digit == nums[j]:
            count += 1
        else:
            prenum += str(count)
            prenum += digit
            digit = nums[j]
            count = 1
    prenum += str(count)
    prenum += digit
    nums = prenum
