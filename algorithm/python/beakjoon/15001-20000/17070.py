# 17070
# https://www.acmicpc.net/problem/17070

from sys import stdin

HORIZONTAL = 0
VERTICAL = 1
CROSS = 2

n = int(stdin.readline())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
dp[HORIZONTAL][0][1] = 1
for i in range(2, n):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
    for c in range(1, n):
        if board[r][c] == 0:
            dp[VERTICAL][r][c] = dp[VERTICAL][r-1][c] + dp[CROSS][r-1][c]
            dp[HORIZONTAL][r][c] = dp[HORIZONTAL][r][c-1] + dp[CROSS][r][c-1]

            if board[r-1][c] == 0 and board[r][c-1] == 0:
                dp[CROSS][r][c] = dp[HORIZONTAL][r-1][c-1] + dp[VERTICAL][r-1][c-1] + dp[CROSS][r-1][c-1]


print(dp[VERTICAL][n-1][n-1] + dp[HORIZONTAL][n-1][n-1]  + dp[CROSS][n-1][n-1] )

