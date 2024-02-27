# 2360
# https://www.acmicpc.net/problem/2630

from sys import stdin

WHITE = 0
BLUE = 1

N = int(stdin.readline())
colors = [0, 0] # 0 = white, 1 = blue

matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]

def check(rs, re, cs, ce):
    target = matrix[rs][cs]

    for row in range(rs, re):
        for col in range(cs, ce):
            if matrix[row][col] != target:
                return -1

    return target

def cut(rs, re, cs, ce):
    rm = (rs + re) // 2
    cm = (cs + ce) // 2

    left_top = (rs, rm, cs, cm)
    right_top = (rs, rm, cm, ce)
    left_bottom = (rm, re, cs, cm)
    right_bottom = (rm, re, cm, ce)

    return (left_top, right_top, left_bottom, right_bottom)

def solution(rs, re, cs, ce):
    check_result = check(rs, re, cs, ce)

    if check_result >= 0:
        colors[check_result] += 1
    else:
        parts = cut(rs, re, cs, ce)

        for part in parts:
            part_rs, part_re, part_cs, part_ce = part
            solution(part_rs, part_re, part_cs, part_ce)


solution(0, N, 0, N)

print(colors[WHITE])
print(colors[BLUE])