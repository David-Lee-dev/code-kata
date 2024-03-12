# 11403
# https://www.acmicpc.net/problem/11403


from sys import stdin

n = int(input())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
table = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        table[i][j] = graph[i][j]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if (table[i][k] == 1 and table[k][j] == 1) or table[i][j]:
                table[i][j] = 1

for i in range(n):
    for j in range(n):
        print(table[i][j], end=' ')
    print()

