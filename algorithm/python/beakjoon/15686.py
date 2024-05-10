# 15686
# https://www.acmicpc.net/problem/15686

from sys import stdin

n, m = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]

homes = []
bbqs = []

result = n**4

for r in range(n):
    for c in range(n):
        if matrix[r][c] == 1:
            homes.append((r + 1, c + 1))
        elif matrix[r][c] == 2:
            bbqs.append((r + 1, c + 1))


def calc(alives):
    result = 0

    for ho in homes:
        candi = []
        for al in alives:
            candi.append(abs(al[0] - ho[0]) + abs(al[1] - ho[1]))
        result += min(candi)
    return result


def solution(idx, cnt, alives):
    global result

    if cnt == m:
        result = min(result, calc(alives))
        return

    if idx == len(bbqs):
        if alives:
            result = min(result, calc(alives))
        return

    alives.append(bbqs[idx])
    solution(idx + 1, cnt + 1, alives)
    alives.pop()
    solution(idx + 1, cnt, alives)

solution(0, 0, [])
print(result)
