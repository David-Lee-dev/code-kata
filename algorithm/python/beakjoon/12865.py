# 12865
# https://www.acmicpc.net/problem/12865

from sys import stdin

WEIGHT = 0
VALUE = 1

n, k = map(int, stdin.readline().split())
stuffs = []
result = []
for _ in range(n):
    stuffs.append(tuple(map(int, stdin.readline().split())))

result = [[0] * n for _ in range(k + 1)]

for stuff_index in range(n):
    for remained_bag_weight in range(k + 1):
        stuff = stuffs[stuff_index]

        if stuff[WEIGHT] > remained_bag_weight:
            result[remained_bag_weight][stuff_index] = 0 if stuff_index < 1 else result[remained_bag_weight][stuff_index - 1]
        else:
            result[remained_bag_weight][stuff_index] = stuff[VALUE] if stuff_index == 0 else max(result[remained_bag_weight][stuff_index - 1], stuff[VALUE] + result[remained_bag_weight - stuff[WEIGHT]][stuff_index - 1])


print(result[-1][-1])