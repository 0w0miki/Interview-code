n = int(input(""))
mat = []
for i in range(n):
    line = input()
    line = line.split(' ')
    mat.append(line)
m = int(input(""))
times = m % 4
if times == 0:
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print("")
elif times == 1:
    for j in range(n):
        for i in range(n-1,-1,-1):
            print(mat[i][j], end=" ")
        print("")
elif times == 2:
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            print(mat[i][j], end=" ")
        print("")
elif times == 3:
    for j in range(n-1,-1,-1):
        for i in range(n):
            print(mat[i][j], end=" ")
        print("")

# zbf
# import numpy as np

# n = int(input())
# l = []
# for i in range(n):
#     one = str(input()).split(' ')
#     o = [int(t) for t in one]
#     l.append(o)

# m = int(input())

# m = m % 4

# l = np.array(l)
# if n >= 2:
#     if m != 0:
#         for _ in range(4-m):
#             l = np.rot90(l)
# for i in range(n):
#     for j in range(n):
#         print(l[i,j],end=" ")
#     print('')