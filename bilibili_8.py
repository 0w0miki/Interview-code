while True:
    string = input().split(" ")
    m = int(string[0])
    n = int(string[1])
    if m == -1 and n == -1:
        break
    mat = []
    for i in range(n):
        row = input().split(" ")
        mat.append(row)
    up, right, left, down = 0, n-1, 0, m-1
    count, size = 0, n*m
    while(up < down or left < right):
        # up
        for i in range(left, right+1):
            if count != size - 1:
                print(mat[up][i],end=",")
            else:
                print(mat[up][i])
            count += 1
        up += 1
        # right
        for i in range(up, down+1):
            if count != size - 1:
                print(mat[right][i],end=",")
            else:
                print(mat[right][i])
            count += 1
        if count > size:break
        right -= 1
        # down
        for i in range(right, left-1, -1):
            if count != size - 1:
                print(mat[down][i],end=",")
            else:
                print(mat[down][i])
            count += 1
        if count > size:break
        down -= 1
        # left
        for i in range(down, up-1, -1):
            if count != size - 1:
                print(mat[left][i],end=",")
            else:
                print(mat[left][i])
            count += 1
        if count > size:break
        left += 1
        
        