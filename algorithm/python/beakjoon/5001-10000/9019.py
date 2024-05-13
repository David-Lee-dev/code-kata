# 9019
# https://www.acmicpc.net/problem/9019

from sys import stdin
from collections import deque

T = int(stdin.readline())

commends = ['D', 'S', 'L', 'R']

def commend_D(num):
    return (2 * num) % 10000


def commend_S(num):
    if num < 1:
        return 9999

    return num - 1

def commend_L(num):
     return ((num % 1000) * 10) + (num // 1000)


def commend_R(num):
    return ((num % 10) * 1000) + (num // 10)


def execute_commend(commend, num):
    if commend == 'D':
        return commend_D(num)
    elif commend == 'S':
        return commend_S(num)
    elif commend == 'R':
        return commend_R(num)
    elif commend == 'L':
        return commend_L(num)


for _ in range(T):
    a, b = map(int, stdin.readline().split())

    check_list = [False] * 10000
    check_list[a] = True
    queue = deque([(a, '')])

    result = None

    while queue:
        now, process = queue.popleft()

        if now == b:
            result = process
            break

        for c in commends:
            converted = execute_commend(c, now)

            if check_list[converted]:
                continue

            check_list[converted] = True
            queue.append((converted, process + c))

    print(result)