# 9465
# https://www.acmicpc.net/problem/9465

from sys import stdin
tc = int(stdin.readline())

for _ in range(tc):
    n = int(stdin.readline())

    matrix = [
        list(map(int, stdin.readline().split())),
        list(map(int, stdin.readline().split()))
    ]

    result = [
        [0] * n,
        [0] * n
    ]
    max1 = max2 = 0

    for i in range(n):
        if i >= 2:
            result[0][i] = matrix[0][i] + max(result[1][i - 1], result[1][i - 2])
            result[1][i] = matrix[1][i] + max(result[0][i - 1], result[0][i - 2])
        elif i == 1:
            result[0][1] = matrix[1][0] + matrix[0][1]
            result[1][1] = matrix[0][0] + matrix[1][1]
        else:
            result[0][0] = matrix[0][0]
            result[1][0] = matrix[1][0]

        if result[0][i] > max1:
            max1 = result[0][i]
        if result[1][i] > max2:
            max2 = result[1][i]

    print(max(max1, max2))

