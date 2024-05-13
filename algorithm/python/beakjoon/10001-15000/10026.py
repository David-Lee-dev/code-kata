# 10026
# https://www.acmicpc.net/problem/10026
import pprint
from sys import stdin
import sys
sys.setrecursionlimit(10**6)

RED = 'R'
GREEN = 'G'
BLUE = 'B'

ROW = NORMAL = 0
COL = COLOR_BLIND = 1

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
results = [0, 0]

n = int(input())
picture = [stdin.readline() for _ in range(n)]
visited = [[[False] * n for _ in range(n)] for _ in range(2)]


def check_color_for_normal(row, col, color):
    if picture[row][col] == color:
        return True

    return False


def check_color_for_blind(row, col, color):
    if color == RED or color == GREEN:
        if picture[row][col] == RED or picture[row][col] == GREEN:
            return True
        else:
            return False
    else:
        if picture[row][col] == BLUE:
            return True
        else:
            return False


def DFS(row, col, type, color):

    for d in directions:
        nxt_row = row + d[ROW]
        nxt_col = col + d[COL]

        if not (0 <= nxt_row < n):
            continue
        if not (0 <= nxt_col < n):
            continue
        if visited[type][nxt_row][nxt_col]:
            continue

        if type == NORMAL and check_color_for_normal(nxt_row, nxt_col, color):
            visited[NORMAL][nxt_row][nxt_col] = True
            DFS(nxt_row, nxt_col, NORMAL, color)
        elif type == COLOR_BLIND and check_color_for_blind(nxt_row, nxt_col, color):
            visited[COLOR_BLIND][nxt_row][nxt_col] = True
            DFS(nxt_row, nxt_col, COLOR_BLIND, color)


for r in range(n):
    for c in range(n):
        if not visited[NORMAL][r][c]:
            visited[NORMAL][r][c] = True
            DFS(r, c, NORMAL, picture[r][c])
            results[NORMAL] += 1
        if not visited[COLOR_BLIND][r][c]:
            visited[COLOR_BLIND][r][c] = True
            DFS(r, c, COLOR_BLIND, picture[r][c])
            results[COLOR_BLIND] += 1


print(f'{results[NORMAL]} {results[COLOR_BLIND]}')