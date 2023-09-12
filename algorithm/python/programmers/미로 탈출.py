# 미로 탈출
# https://school.programmers.co.kr/learn/courses/30/lessons/159993#

from collections import deque

delta_row = [-1, 1, 0, 0]
delta_col = [0, 0, -1, 1]

WALL = 'X'
LOAD = 'O'
LEVER = 'L'
EXIT = 'E'

def find_target(row, col, maps, target):
    ROW = len(maps)
    COL = len(maps[0])

    matrix = [list(maps[r]) for r in range(ROW)]
    matrix[row][col] = WALL
    queue = deque([(row, col, 0)])

    while(queue):
        r, c , cnt = queue.popleft()

        for i in range(4):
            nxt_r = r + delta_row[i]
            nxt_c = c + delta_col[i]

            if not (0 <= nxt_r < ROW):
                continue
            if not (0 <= nxt_c < COL):
                continue
            if matrix[nxt_r][nxt_c] == WALL:
                continue
            if matrix[nxt_r][nxt_c] == target:
                return (nxt_r, nxt_c, cnt + 1)

            queue.append((nxt_r, nxt_c, cnt + 1))
            matrix[nxt_r][nxt_c] = WALL

    return (-1, -1, -1)


def find_start(maps):
    ROW = len(maps)
    COL = len(maps[0])

    for r in range(ROW):
        for c in range(COL):
            if maps[r][c] == 'S':
                start = (r, c)
                return (r, c)

    return (-1, -1)


def solution(maps):
    answer = 0

    start_r, start_c = find_start(maps)
    start_r, start_c, cnt = find_target(start_r, start_c, maps, LEVER)

    if cnt < 0: return - 1
    answer += cnt

    cnt = find_target(start_r, start_c, maps, EXIT)[2]
    if cnt < 0: return - 1
    return answer + cnt
