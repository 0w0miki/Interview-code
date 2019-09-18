def allocate(n,k):
    if k == 1:
        return [n]
    if n == 0:
        return [0] * k
    table = []
    for i in range(n+1):
        # 第1个人分配到i个礼物
        t1 = allocate(n-i,k-1)
        if type(t1[0]) == list:
            for j in range(len(t1)):
                t1[j].insert(0,i)
        else:
            t1.insert(0,i)
            t1 = [t1]
        if table == []:
            table = t1
        else:
            table += t1
    return table

n = 10
k = 10
res = 0

if n == 0:
    print("0\n")
    for i in range(k):
        print("|")



table = allocate(n,k)
print(len(table))
for i in range(len(table)):
    for j in range(k):
        for m in range(table[i][j]):
            print("*", end='')
        if j != k-1:
            print("|", end='')
    print("")