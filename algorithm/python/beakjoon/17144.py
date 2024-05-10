# 17144
# https://www.acmicpc.net/problem/17144

from sys import stdin
row, col, time = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(row)]
miair = None
for r in range(row):
    for c in range(col):
        if matrix[r][c] == -1:
            miair = [(r, c), (r + 1, c)]
            break
    if miair:
        break


def get_dust_points(matrix):
    points = []
    for r in range(row):
        for c in range(col):
            if matrix[r][c] > 0:
                points.append((r, c, matrix[r][c]))
    return points


def spread_dust(matrix, points):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    spread_matrix = [[[] for _ in range(col)] for _ in range(row)]
    for p in points:
        count = 0
        dust_for_spread = int(p[2] / 5)

        for d in delta:
            nxt_r = p[0] + d[0]
            nxt_c = p[1] + d[1]

            if not (0 <= nxt_r < row):
                continue
            if not (0 <= nxt_c < col):
                continue
            if matrix[nxt_r][nxt_c] == -1:
                continue

            count += 1
            spread_matrix[nxt_r][nxt_c].append(dust_for_spread)
        spread_matrix[p[0]][p[1]].append(matrix[p[0]][p[1]] - (dust_for_spread * count))

    for r in range(row):
        for c in range(col):
            if matrix[r][c] >= 0:
                matrix[r][c] = sum(spread_matrix[r][c])


# circulate air
def circulate_top(matrix, circulator_point):
    cir_r, cir_c = circulator_point

    for r in range(cir_r - 1, 0, -1):
        matrix[r][cir_c] = matrix[r - 1][cir_c]
    else:
        matrix[r - 1][cir_c] = 0

    for c in range(0, col - 1):
        matrix[0][c] = matrix[0][c + 1]
    else:
        matrix[0][c + 1] = 0

    for r in range(0, cir_r):
        matrix[r][col - 1] = matrix[r + 1][col - 1]
    else:
        matrix[r + 1][col - 1] = 0

    for c in range(col - 1, 1, -1):
        matrix[cir_r][c] = matrix[cir_r][c - 1]
    else:
        matrix[cir_r][c - 1] = 0

def circulate_bottom(matrix, circulator_point):
    cir_r, cir_c = circulator_point

    for r in range(cir_r + 1, row - 1):
        matrix[r][cir_c] = matrix[r + 1][cir_c]

    for c in range(0, col - 1):
        matrix[row - 1][c] = matrix[row - 1][c + 1]
    else:
        matrix[row - 1][c + 1] = 0

    for r in range(row - 1, cir_r, -1):
        matrix[r][col - 1] = matrix[r - 1][col - 1]
    else:
        matrix[cir_r][col - 1] = 0

    for c in range(col - 1, 1, -1):
        matrix[cir_r][c] = matrix[cir_r][c - 1]
    else:
        matrix[cir_r][c - 1] = 0


for _ in range(time):
    points = get_dust_points(matrix)
    spread_dust(matrix, points)
    circulate_top(matrix, miair[0])
    circulate_bottom(matrix, miair[1])

result = 2
for r in range(row):
    for c in range(col):
        result += matrix[r][c]

print(result)