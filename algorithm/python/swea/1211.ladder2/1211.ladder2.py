# 1211.ladder2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14BgD6AEECFAYh&categoryId=AV14BgD6AEECFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=2

from collections import deque
import sys
sys.stdin = open("input.txt", "r")

DOWN = 0
LEFT = 1
RIGHT = 2

for test_case in range(1, 11):
    T = int(input())

    matrix = [list(map(int, input().split())) for _ in range(100)]

    q = deque([])
    for c in range(len(matrix[0])):
        if matrix[0][c] == 1:
            # row, col, direction, count, start point
            q.append((0, c, 0, 0, c))

    result = 0
    while q:
        r, c, direction, cnt, sp = q.popleft()

        if r == 99:
            result = sp
            break

        # 좌우 확인
        if direction is RIGHT and c + 1 < 100 and matrix[r][c + 1] == 1:
            q.append((r, c + 1, RIGHT, cnt + 1, sp))
            continue
        elif direction is LEFT and c - 1 >= 0 and matrix[r][c - 1] == 1:
            q.append((r, c - 1, LEFT, cnt + 1, sp))
            continue

        if direction is DOWN:
            if c + 1 < 100 and matrix[r][c + 1] == 1:
                q.append((r, c + 1, RIGHT, cnt + 1, sp))
                continue
            elif c - 1 >= 0 and matrix[r][c - 1] == 1:
                q.append((r, c - 1, LEFT, cnt + 1, sp))
                continue

        q.append((r + 1, c, DOWN, cnt + 1, sp))

    print(f'#{test_case} {result}')
