# 디펜스 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/142085


import heapq


def solution(n, k, enemy):
    te = 0
    h = []

    for i, e in enumerate(enemy):
        te += e
        heapq.heappush(h, -e)

        if te > n:
            if k == 0:
                return i
            te += heapq.heappop(h)
            k -= 1

    return i + 1
