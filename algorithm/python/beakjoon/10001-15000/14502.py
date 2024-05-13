# 14502
# https://www.acmicpc.net/problem/14502

from sys import stdin
from collections import deque
from copy import deepcopy

n, m = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0

def spread():
    matrix_clone = deepcopy(matrix)
    birus = deque([])
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 2:
                birus.append((r, c))

    while birus:
        r, c = birus.popleft()

        for d in direction:
            nr = r + d[0]
            nc = c + d[1]

            if not (0 <= nr < n):
                continue
            if not (0 <= nc < m):
                continue
            if matrix_clone[nr][nc] > 0:
                continue

            birus.append((nr, nc))
            matrix_clone[nr][nc] = 2

    count = 0
    for r in range(n):
        for c in range(m):
            if matrix_clone[r][c] > 0:
                count += 1

    return count

def build_wall(row, col, remain):
    global result

    if remain == 0:
        infect_count = spread()
        result = max(result, n * m - infect_count)
        return

    for r in range(row, n):
        col_start = col if r == row else 0
        for c in range(col_start, m):
            if matrix[r][c] == 0:
                matrix[r][c] = 1
                build_wall(r, c + 1, remain - 1)
                matrix[r][c] = 0


build_wall(0, 0, 3)

print(result)