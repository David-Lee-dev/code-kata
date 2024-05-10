# 2448
# https://www.acmicpc.net/problem/2448

from collections import deque

row = int(input())
col = int(5 * (row / 3) + (row / 3) - 1)
matrix = [[' '] * col for _ in range(row)]
sp_stack = deque([int(col / 2)])

for r in range(0, row, 3):
    for _ in range(len(sp_stack)):
        c = sp_stack.popleft()

        matrix[r][c] = '*'
        matrix[r + 1][c - 1] = '*'
        matrix[r + 1][c + 1] = '*'

        for i in range(c - 2, c + 3):
            matrix[r + 2][i] = '*'

        if not sp_stack or sp_stack[-1] != c - 3:
            sp_stack.append(c - 3)
        else:
            sp_stack.pop()
        if not sp_stack or sp_stack[-1] != c + 3:
            sp_stack.append(c + 3)
        else:
            sp_stack.pop()

for m in matrix:
    print(''.join(m))