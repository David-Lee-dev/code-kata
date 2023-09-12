# 삼총사
# https://school.programmers.co.kr/learn/courses/30/lessons/131705

answer = 0


def combination(total, cnt, number, idx):
    global answer
    if cnt == 3:
        if total == 0:
            answer += 1
        return

    for i in range(idx + 1, len(number)):
        if idx == i:
            continue

        combination(total + number[i], cnt + 1, number, i)


def solution(number):
    for i in range(len(number)):
        combination(number[i], 1, number, i)

    return answer
