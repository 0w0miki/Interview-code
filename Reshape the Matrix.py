# input
nums = [[1,2,3],[3,4,5]]
r = 3
c = 2
# algorithm
row = len(nums)
col = len(nums[0])
m = []
mat = []
if r*c != row*col:
    print(nums)
else:
    for i in range(row):
        m += nums[i]
    for i in range(r):
        mat.append(m[c*i:c*i+c])
    print(mat)
