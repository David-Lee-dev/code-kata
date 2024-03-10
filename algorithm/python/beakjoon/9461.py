# 9461
# https://www.acmicpc.net/problem/9461

t = int(input())
dp = [1, 1, 1]
dp.extend([0] * 97)

for i in range(3, 100):
    dp[i] = dp[i - 3] + dp[i - 2]
print(dp)

for _ in range(t):
    n = int(input())
    print(dp[n - 1])
