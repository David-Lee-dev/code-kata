# 숫자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque


def solution(x, y, n):
    cnt = 0
    q = deque([(y, cnt)])

    while q:
        now, cnt = q.popleft()

        if now == x:
            return cnt

        if now % 3 == 0 and now // 3 >= x:
            q.append((now // 3, cnt + 1))
        if now % 2 == 0 and now // 2 >= x:
            q.append((now // 2, cnt + 1))
        if now - n >= x:
            q.append((now - n, cnt + 1))

    return -1
