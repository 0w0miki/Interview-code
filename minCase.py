weight = int(input())
resTab = [10000,
10000,
10000,
1,
10000,
1,
2,
1]
if weight >= 8:
    resTab += [0] * (weight - 7)
    for w in range(8, weight+1):
        resTab[w] = min(resTab[w-3], resTab[w-5], resTab[w-7]) + 1
if resTab[weight] < 10000:
    print(resTab[weight])
else:
    print(-1)