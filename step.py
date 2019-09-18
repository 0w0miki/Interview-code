'''
已知深渊有N层台阶构成（1 <= N <= 1000)，并且每次月神仅可往上爬2的整数次幂个台阶(1、2、4、....)，请你编程告诉月神，月神有多少种方法爬出深渊 

input:
输入共有M行，(1<=M<=1000)
第一行输入一个数M表示有多少组测试数据，
接着有M行，每一行都输入一个N表示深渊的台阶数

output:
输出可能的爬出深渊的方式
'''
table = [0] * 1000
table[0], table[1]=1, 1
expo_2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
max_index = 1
for i in range(2, 1000):
    if max_index < 10 and i >= expo_2[max_index]:
        max_index += 1
    for j in range(max_index):
        table[i] += table[i-expo_2[j]]
        # table[i] %= 1000000003

print(table)

N = int(input())
for i in range(N):
    num = int(input())
    print(table[num])