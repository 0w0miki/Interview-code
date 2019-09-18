'''
如果一个积木A的长和宽都不大于另外一个积木B的长和宽，则积木A可以搭在积木B的上面
这一袋子积木最多可以搭多少层
input:
第一行为积木的总个数 N
之后一共有N行，分别对应于每一个积木的宽W和长L
output:
输出总共可以搭的层数
'''

import bisect
import sys

N = int(input())
bricks = []
for i in range(N):
    W, L = map(int, input().strip().split())
    bricks.append((W, L))
# bricks = sorted(bricks, key = lambda x: x[1])
bricks = sorted(bricks, key = lambda x: x[0])
Longest = []
for brick in bricks:
    if Longest == []:
        Longest.append(brick[1])
    elif brick[1] >= Longest[-1]:
        Longest.append(brick[1])
    else:
        index = bisect.bisect(Longest, brick[1])
        Longest[index] = brick[1]

print(len(Longest), Longest)
