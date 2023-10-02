# 1227.미로2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14wL9KAGkCFAYD&categoryId=AV14wL9KAGkCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=2


from collections import deque
import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    case = int(input())
    delta_row = [-1, 1, 0, 0]
    delta_col = [0, 0, -1, 1]

    matrix = []
    visit = [[False] * 100 for _ in range(100)]
    start = None
    end = None
    for r in range(100):
        tmp = list(map(int, input()))
        for c in range(100):
            if tmp[c] == 2:
                start = (r, c)
            if tmp[c] == 3:
                end = (r, c)

        matrix.append(tmp)

    q = deque([start])

    result = 0
    while q:
        r, c = q.popleft()

        if (r, c) == end:
            result = 1
            break

        for i in range(4):
            nxt_r = r + delta_row[i]
            nxt_c = c + delta_col[i]

            if not (0 <= nxt_r < 100):
                continue
            if not (0 <= nxt_c < 100):
                continue
            if matrix[nxt_r][nxt_c] == 1:
                continue
            if visit[nxt_r][nxt_c]:
                continue

            q.append((nxt_r, nxt_c))
            visit[nxt_r][nxt_c] = True

    print(f'${case} {result}')
