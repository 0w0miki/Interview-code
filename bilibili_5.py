n = int(input())
wapons = input().split(" ")
wapons = list(map(int,wapons))
guestnum = int(input())
ranges = []
for i in range(guestnum):
    r = input().split(" ")
    r = list(map(int,r))
    ranges.append(r)
count = 0
for r in ranges:
    if r[1] - r[0] < 2:
        continue
    right = r[1]-1 if r[1] < len(wapons) else len(wapons)-1
    left = r[0]-1 if r[0] > 0 else 0
    w = wapons[left:right+1]
    w.sort()
    if w[-1] < w[-2] + w[0]:
        count += 1
print(count)