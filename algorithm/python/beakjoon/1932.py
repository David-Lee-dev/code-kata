# 1932
# https://www.acmicpc.net/problem/1932

from sys import stdin

n = int(stdin.readline())
nums = []
for _ in range(n):
    nums.extend(list(map(int, stdin.readline().split())))
dp = [nums[0]]
level = 2
cur_idx = 1
while level <= n:
    for l in range(level):
        top_left_idx = cur_idx - level
        top_right_idx = cur_idx - level + 1
        if l == 0:
            dp.append(dp[top_right_idx] + nums[cur_idx])
        elif l == level - 1:
            dp.append(dp[top_left_idx] + nums[cur_idx])
        else:
            dp.append(max(dp[top_right_idx] + nums[cur_idx], dp[top_left_idx] + nums[cur_idx]))
        cur_idx += 1
    level += 1

print(max(dp[-n:]))