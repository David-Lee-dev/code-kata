# 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

SEA = 'X'
delta_row = [-1, 1, 0, 0]
delta_col = [0, 0, -1, 1]

def check(matrix, row, col, ROW, COL):

    result = 0
    queue = deque([[matrix[row][col], row, col]])
    matrix[row][col] = 'X'

    while queue:
        now, row, col = queue.popleft()
        result += int(now)

        for i in range(4):
            nxt_row = row + delta_row[i]
            nxt_col = col + delta_col[i]

            if not (0 <= nxt_row < ROW): continue
            if not (0 <= nxt_col < COL): continue
            if matrix[nxt_row][nxt_col] == SEA: continue

            queue.append([matrix[nxt_row][nxt_col], nxt_row, nxt_col])
            matrix[nxt_row][nxt_col] = 'X'

    return result

def solution(maps):
    matrix = []

    for m in maps:
        matrix.append(list(m))

    ROW = len(matrix)
    COL = len(matrix[0])

    answer = []

    for r in range(ROW):
        for c in range(COL):
            if matrix[r][c] == SEA:
                continue

            answer.append(check(matrix, r, c, ROW, COL))

    return sorted(answer) if answer else [-1]
