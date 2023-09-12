# 리코쳇 로봇
# https://school.programmers.co.kr/learn/courses/30/lessons/169199#

from collections import deque

delta_row = [-1, 1, 0, 0]
delta_col = [0, 0, -1, 1]
CHECKED = 'C'

def go(board, r, c, dir_r, dir_c, ROW, COL):

    while True:
        r += dir_r
        c += dir_c

        if not (0 <= r < ROW):
            break
        if not (0 <= c < COL):
            break
        if board[r][c] == 'D':
            break

    return (r - dir_r, c - dir_c)

def solution(board):
    ROW = len(board)
    COL = len(board[0])

    queue = deque([])
    goal = None

    for i in range(ROW):
        board[i] = list(board[i])

    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == 'R':
                board[r][c] = CHECKED
                queue.append((r, c, 0))
            if board[r][c] == 'G':
                goal = (r, c)

            if len(queue) > 0 and goal:
                break
        if len(queue) > 0 and goal:
            break

    while queue:
        r, c, cnt = queue.popleft()

        if board[r][c] == 'G':
            return cnt

        for i in range(4):
            tmp_r, tmp_c = go(board, r, c, delta_row[i], delta_col[i], ROW, COL)

            if r == tmp_r and c == tmp_c:
                continue
            if board[tmp_r][tmp_c] == CHECKED:
                continue

            queue.append((tmp_r, tmp_c, cnt + 1))
            if board[tmp_r][tmp_c] != 'G':
                board[tmp_r][tmp_c] = CHECKED

    return -1
