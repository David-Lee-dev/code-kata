# 18870
# https://www.acmicpc.net/problem/18870

N = int(input())
arr = list(map(int, input().split()))
nums = sorted(list(set(arr)))
table = {}

for i, n in enumerate(nums):
    table[n] = i

for e in arr:
    print(f'{table[e]}', end=' ')