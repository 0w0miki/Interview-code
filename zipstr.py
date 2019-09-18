string = input()
count = 0
lastc = string[0]
for c in string:
    if c == lastc:
        count += 1
    else:
        print(str(count)+lastc, end = '')
        lastc = c
        count = 1
print(str(count)+lastc, end = '')