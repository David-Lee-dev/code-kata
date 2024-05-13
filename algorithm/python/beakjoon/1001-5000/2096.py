# 2096
# https://www.acmicpc.net/problem/2096
import sys
from sys import stdin

n = int(stdin.readline())

max_result = [[0] * 3 for _ in range(2)]
min_result = [[-1] * 3 for _ in range(2)]

prev_idx = 0
nxt_idx = 1

init_arr = list(map(int, stdin.readline().split()))
for c in range(3):
    max_result[prev_idx][c] = init_arr[c]
    min_result[prev_idx][c] = init_arr[c]

for r in range(n - 1):
    input_arr = list(map(int, stdin.readline().split()))

    for c in range(3):
        col_list = [c - 1, c, c + 1]

        for nxt_c in col_list:
            if nxt_c < 0 or nxt_c >= 3:
                continue

            max_nxt_cost = max_result[prev_idx][c] + input_arr[nxt_c]
            if max_result[nxt_idx][nxt_c] < max_nxt_cost:
                max_result[nxt_idx][nxt_c] = max_nxt_cost

            min_nxt_cost = min_result[prev_idx][c] + input_arr[nxt_c]
            if min_result[nxt_idx][nxt_c] == -1 or min_result[nxt_idx][nxt_c] > min_nxt_cost:
                min_result[nxt_idx][nxt_c] = min_nxt_cost

    prev_idx, nxt_idx = nxt_idx, prev_idx

    for c in range(3):
        max_result[nxt_idx][c] = 0
        min_result[nxt_idx][c] = -1

print(f'{max(max_result[prev_idx])} {min(min_result[prev_idx])}')

