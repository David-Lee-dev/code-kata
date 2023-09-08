# [PCCP 모의고사 #2] 신입사원 교육
# https://school.programmers.co.kr/learn/courses/15009/lessons/121688


import heapq


def solution(ability, number):
    answer = 0

    heapq.heapify(ability)

    for _ in range(number):
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)

        total = a + b

        heapq.heappush(ability, total)
        heapq.heappush(ability, total)

    return sum(ability)
