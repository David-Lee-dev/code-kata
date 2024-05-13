# 11660
# https://www.acmicpc.net/problem/11660

from sys import stdin
n, m = map(int, stdin.readline().split())

matrix = []
for _ in range(n):
    row = list(map(int, stdin.readline().split()))

    for i in range(1, n):
        row[i] = row[i - 1] + row[i]

    matrix.append(row)

for c in range(n):
    for r in range(1, n):
        matrix[r][c] = matrix[r - 1][c] + matrix[r][c]

points = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    points.append((x1 - 1, y1 - 1, x2 - 1, y2 - 1))

for point in points:
    x1, y1, x2, y2 = point
    result = matrix[x2][y2]

    if x1 > 0:
        result -= matrix[x1 - 1][y2]
    if y1 > 0:
        result -= matrix[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        result += matrix[x1 - 1][y1 - 1]

    print(result)