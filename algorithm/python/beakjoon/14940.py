# 14940
# https://www.acmicpc.net/problem/14940

from sys import stdin
from collections import deque

ROW = 0
COL = 1

delta_row = [-1, 1, 0, 0]
delta_col = [0, 0, -1, 1]

n, m = map(int, stdin.readline().split(' '))

matrix = []
visit = [[False] * m for _ in range(n)]
result = [[-1] * m for _ in range(n)]
start = [0, 0]

for row in range(n):
    line = list(map(int, stdin.readline().split()))
    for col in range(m):
        if line[col] == 2:
            start[ROW] = row
            start[COL] = col
        elif line[col] == 0:
            result[row][col] = 0

    matrix.append(line)

queue = deque([(start[ROW], start[COL], 0)])
visit[start[ROW]][start[COL]] = True

while queue:
    r, c, distance = queue.popleft()

    result[r][c] = distance

    for i in range(4):
        nxt_r = r + delta_row[i]
        nxt_c = c + delta_col[i]

        if not (0 <= nxt_r < n and 0 <= nxt_c < m):
            continue
        if matrix[nxt_r][nxt_c] == 0:
            continue
        if visit[nxt_r][nxt_c]:
            continue

        queue.append((nxt_r, nxt_c, distance + 1))
        visit[nxt_r][nxt_c] = True

for line in result:
    for num in line:
        print(num, end=" ")
    print()