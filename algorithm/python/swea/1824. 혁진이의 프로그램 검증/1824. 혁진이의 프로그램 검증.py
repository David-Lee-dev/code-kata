# 1824. 혁진이의 프로그램 검증
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV4yLUiKDUoDFAUx&categoryId=AV4yLUiKDUoDFAUx&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1


from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def under_bar(m):
    if m == 0:
        return '>'

    return '<'


def vertical_bar(m):
    if m == 0:
        return 'v'

    return '^'


def get_next(r, c, direction):
    nxt_r = r + direction[0]
    nxt_c = c + direction[1]

    if nxt_r < 0:
        nxt_r = R - 1
    if nxt_r >= R:
        nxt_r = 0

    if nxt_c < 0:
        nxt_c = C - 1
    if nxt_c >= C:
        nxt_c = 0

    return (nxt_r, nxt_c)


T = int(input())
for test_case in range(1, T + 1):
    R, C = map(int, input().split(' '))

    matrix = [list(input()) for _ in range(R)]
    visit = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            visit[i][j] = []
    visit[0][0] = [(0, '>')]
    q = deque([(0, 0, '>')])

    table = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0),
    }
    memory = 0
    result = 'NO'
    while q:
        r, c, direction = q.pop()
        command = matrix[r][c]

        # 현 위치 처리
        if command == '@':
            result = 'YES'
        elif command == '+':
            memory += 1
            if memory > 15:
                memory = 0
        elif command == '-':
            memory -= 1
            if memory < 0:
                memory = 15
        elif command in '0123456789':
            memory = int(command)
        elif command == '_':
            direction = under_bar(memory)
        elif command == '|':
            direction = vertical_bar(memory)
        elif command in '<>v^':
            direction = command

        for d in '<>^v' if command == '?' else direction:
            nxt_r, nxt_c = get_next(r, c, table[d])

            if (memory, d) in visit[nxt_r][nxt_c]:
                continue

            q.append((nxt_r, nxt_c, d))
            visit[nxt_r][nxt_c].append((memory, d))

    print(f'#{test_case} {result}')