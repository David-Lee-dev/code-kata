# 연속 부분 수열 합의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/131701


from collections import deque
from itertools import islice


def solution(elements):
    answer = 0

    elements = deque(elements)
    result = set()
    for i in range(len(elements)):
        elements.append(elements.popleft())
        result.add(elements[0])
        result.add(elements[0])
        for j in range(1, len(elements)):
            result.add(sum(islice(elements, 0, j)))

    return len(result) + 1