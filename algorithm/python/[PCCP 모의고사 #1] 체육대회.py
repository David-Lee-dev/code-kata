# [PCCP 모의고사 #1] 체육대회
# https://school.programmers.co.kr/learn/courses/15008/lessons/121684


answer = 0


def pick(subject, total, ability, picked):
    global answer

    if subject == len(ability[0]):
        answer = max(answer, total)
        return

    for student in range(len(ability)):
        if picked[student]:
            continue

        picked[student] = True
        pick(subject + 1, total + ability[student][subject], ability, picked)
        picked[student] = False


def solution(ability):
    global answer
    pick(0, 0, ability, [False] * len(ability))
    return answer
