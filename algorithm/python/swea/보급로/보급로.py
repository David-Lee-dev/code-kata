# 보급로
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do


'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = list(list(map(int, list(input()))) for _ in range(N))
    visit = [[-1] * (N) for _ in range(N)]
    visit[0][0] = 0
    start = (0, 0)
    end = (N - 1, N - 1)
    q = deque([(0, 0)])
    delta_row = [-1, 1, 0, 0]
    delta_col = [0, 0, -1, 1]
    while q:
        r, c = q.popleft()

        for i in range(4):
            nxt_r = r + delta_row[i]
            nxt_c = c + delta_col[i]

            if not (0 <= nxt_r < N):
                continue
            if not (0 <= nxt_c < N):
                continue
            if 0 <= visit[nxt_r][nxt_c] <= visit[r][c] + matrix[nxt_r][nxt_c]:
                continue

            q.append((nxt_r, nxt_c))
            visit[nxt_r][nxt_c] = visit[r][c] + matrix[nxt_r][nxt_c]
    print(f'#{test_case} {visit[N - 1][N - 1]}')