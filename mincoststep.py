costs = list(map(int, input().strip().split(',')))
L = len(costs)
dp = [0] * (L+1)

for i in range(2, L+1):
    dp[i] = min(dp[i-1]+costs[i-1], dp[i-2]+costs[i-2])
print(dp[-1])