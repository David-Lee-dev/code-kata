# 저주의 숫자 3
# https://school.programmers.co.kr/learn/courses/30/lessons/120871


def solution(n):
    answer = 0

    idx = 1
    while idx <= n:
        if answer % 3 == 0 or "3" in str(answer):
            answer += 1
        else:
            idx += 1
            answer += 1

    return answer - 1
