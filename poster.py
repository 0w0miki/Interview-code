# TODO optimize with binary search
def updateList(in_list, index, newer):
    older = in_list[index]
    if newer[0] < older[0]:
        if newer[1] < older[0]:
            return 0
        elif newer[1] < older[1]:
            older[0] = newer[1]
        else:
            post_id = in_list.pop(index)[2]
            return -1
    elif newer[0] < older[1]:
        if newer[1] < older[1]:
            post_id = in_list.pop(index)[2]
            in_list.insert(index, [newer[1], older[1], post_id])
            in_list.insert(index, [older[0], newer[0], post_id])
            return 1
        else:
            older[1] = newer[0]
    return 0

toplist = []
n = int(input())
# post_state = [1] * n
for i in range(n):
    newpost = list(map(int, input().split())) + [i]
    if not toplist:
        toplist.append(newpost)
    else:
        i, l = 0, len(toplist)
        while i < l:
            r = updateList(toplist, i, newpost)
            i += r + 1
            l += r 

        toplist.append(newpost)
# print(toplist)
# print(post_state)
print(len(set([x[2] for x in toplist])))