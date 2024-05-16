# 1005
# https://www.acmicpc.net/problem/1005

from sys import stdin
from heapq import heappush, heappop

t = int(stdin.readline())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    time_list = [0] + list(map(int, stdin.readline().split()))
    out_list = [[] for _ in range(n + 1)]
    in_list = [set() for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, stdin.readline().split())
        out_list[a].append(b)
        in_list[b].add(a)
    w = int(stdin.readline())

    q = []
    for idx in range(1, n + 1):
        if len(in_list[idx]) == 0:
            heappush(q, [time_list[idx], idx])

    result = 0
    while q:
        time, node = heappop(q)

        result += time

        if(node == w):
            print(result)
            break

        for item in q:
            item[0] -= time

        for nxt in out_list[node]:
            in_list[nxt].discard(node)

            if len(in_list[nxt]) == 0:
                heappush(q, [time_list[nxt], nxt])