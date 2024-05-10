# 2638
# https://www.acmicpc.net/problem/2638

from sys import stdin

import sys
sys.setrecursionlimit(1000000)

n, m = map(int, stdin.readline().split())
cnt = 0
cheeze = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = None
expose_table = None
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for r in range(n):
    for c in range(m):
        if cheeze[r][c] == 1:
            cnt += 1


# 외부 공기 스캔
def scan_external_air(row, col):
    for d in directions:
        nxt_row = row + d[0]
        nxt_col = col + d[1]

        if not (0 <= nxt_row < n) or not (0 <= nxt_col < m):
            continue

        if cheeze[nxt_row][nxt_col] == 1:
            if expose_table.get(f'{nxt_row}-{nxt_col}'):
                expose_table[f'{nxt_row}-{nxt_col}'] += 1
            else:
                expose_table[f'{nxt_row}-{nxt_col}'] = 1


def dfs_air(row, col):
    scan_external_air(row, col)

    for d in directions:
        nxt_row = row + d[0]
        nxt_col = col + d[1]

        if not (0 <= nxt_row < n) or not (0 <= nxt_col < m):
            continue
        if cheeze[nxt_row][nxt_col] == 1:
            continue
        if visited[nxt_row][nxt_col]:
            continue

        visited[nxt_row][nxt_col] = True
        dfs_air(nxt_row, nxt_col)


def remove_cheeze():
    result = 0

    for key, value in expose_table.items():
        if value >= 2:
            r, c = map(int, key.split('-'))
            cheeze[r][c] = 0
            result += 1

    return result

time = 0
while cnt > 0:
    expose_table = {}
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    dfs_air(0, 0)
    cnt -= remove_cheeze()
    time += 1

print(time)


