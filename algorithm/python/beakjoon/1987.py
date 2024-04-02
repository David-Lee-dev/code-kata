# 1987
# https://www.acmicpc.net/problem/1987

from sys import stdin

row, col = map(int, stdin.readline().split())
matrix = [stdin.readline() for _ in range(row)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
history = [False] * 26
result = 0
def DFS(r, c, count):
    global result

    if result < count:
        result = count

    for d in directions:
        nxt_r = r + d[0]
        nxt_c = c + d[1]

        if not (0 <= nxt_r < row and 0 <= nxt_c < col):
            continue
        if history[ord(matrix[nxt_r][nxt_c]) - 65]:
            continue

        history[ord(matrix[nxt_r][nxt_c]) - 65] = True
        DFS(nxt_r, nxt_c, count + 1)
        history[ord(matrix[nxt_r][nxt_c]) - 65] = False

history[ord(matrix[0][0]) - 65] = True
DFS(0, 0, 1)

print(result)