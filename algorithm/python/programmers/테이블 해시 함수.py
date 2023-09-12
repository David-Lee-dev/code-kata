# 테이블 해시 함수
# https://school.programmers.co.kr/learn/courses/30/lessons/147354
# programmers


def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=lambda x: [x[col - 1], -x[0]])
    arr = []
    for i in range(row_begin - 1, row_end):
        tmp = 0
        for n in data[i]:
            tmp += n % (i + 1)
        answer ^= tmp

    return answer
