# [PCCP 모의고사 #1] 외톨이 알파벳
# https://school.programmers.co.kr/learn/courses/15008/lessons/121683?language=python3


CNT = 0
PART = 1


def solution(input_string):
    answer = 0
    stack = []
    check = set()
    lonly = set()

    for w in input_string:
        if not stack:
            stack.append(w)

        if stack[-1] != w:
            if w in check:
                lonly.add(w)

            stack.append(w)

        check.add(w)

    answer = list(lonly)
    answer.sort()
    return "".join(answer) if answer else "N"
