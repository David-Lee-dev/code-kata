# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476?language=python3


import heapq


def solution(k, tangerine):
    answer = 0

    table = {}

    for t in tangerine:
        key = str(t)
        if table.get(key):
            table[key] += 1
        else:
            table[key] = 1

    q = []
    for key in table.keys():
        heapq.heappush(q, (-table[key], key))

    while k > 0:
        k += heapq.heappop(q)[0]
        answer += 1
    return answer
