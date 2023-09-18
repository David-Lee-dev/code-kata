# 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265#qna


import heapq
from collections import deque


def solution(topping):
    answer = 0

    tmp = set()
    left_sum_arr = []
    for t in topping:
        tmp.add(t)
        left_sum_arr.append(len(tmp))

    tmp = set()
    right_sum_arr = []
    for i in range(len(topping) - 1, -1, -1):
        tmp.add(topping[i])
        right_sum_arr.append(len(tmp))
    right_sum_arr.reverse()

    for i in range(len(left_sum_arr) - 1):
        if left_sum_arr[i] == right_sum_arr[i + 1]:
            answer += 1

    return answer
