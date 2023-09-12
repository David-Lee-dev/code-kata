# 혼자서 하는 틱택토
# https://school.programmers.co.kr/learn/courses/30/lessons/160585#

delta_row = [-1, 1, 0, 0]
delta_col = [0, 0, -1, 1]


def check_cnt(game):
    o_cnt = 0
    x_cnt = 0

    for r in range(3):
        for c in range(3):
            if game[r][c] == 'O':
                o_cnt += 1
            if game[r][c] == 'X':
                x_cnt += 1

    return [o_cnt, x_cnt]

def check_bingo(game):

    bingo_cross_1 = [0, 0]
    bingo_cross_2 = [0, 0]
    result = [False, False]

    for i in range(3):
        # 가로
        # 세로
        bingo_garo = [0, 0]
        bingo_sero = [0, 0]
        for j in range(3):
            if game[i][j] == 'O':
                bingo_garo[0] += 1
            elif game[i][j] == 'X':
                bingo_garo[1] += 1

            if game[j][i] == 'O':
                bingo_sero[0] += 1
            elif game[j][i] == 'X':
                bingo_sero[1] += 1

        if bingo_garo[0] == 3 or bingo_sero[0] == 3:
            result[0] = True
        if bingo_garo[1] == 3 or bingo_sero[1] == 3:
            result[1] = True

        # 대각선
        if game[i][i] == 'O':
            bingo_cross_1[0] += 1
        elif game[i][i] == 'X':
            bingo_cross_1[1] += 1

        if game[i][2 - i] == 'O':
            bingo_cross_2[0] += 1
        elif game[i][2 - i] == 'X':
            bingo_cross_2[1] += 1

    if bingo_cross_1[0] == 3 or bingo_cross_2[0] == 3:
        result[0] = True
    if bingo_cross_1[1] == 3 or bingo_cross_2[1] == 3:
        result[1] = True

    return result


def solution(board):
    o, x = check_bingo(board)
    o_cnt, x_cnt = check_cnt(board)

    if o:
        if x:
            return 0
        if o_cnt == x_cnt:
            return 0

    if x:
        if o_cnt != x_cnt:
            return 0

    if x_cnt > o_cnt:
        return 0
    if abs(o_cnt - x_cnt) > 1:
        return 0

    return 1
