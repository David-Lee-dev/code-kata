# 13549
# https://www.acmicpc.net/problem/13549

from sys import stdin
from heapq import heappush, heappop

n, k = map(int, stdin.readline().split())
q = [(0, abs(k - n), n)]
visit = [-1] * 200000

while q:
    time, _, now  = heappop(q)

    if now == k:
        print(time)
        break

    nxt_back = now - 1
    if nxt_back >= 0:
        if visit[nxt_back] < 0 or visit[nxt_back] > time + 1:
            heappush(q, (time + 1, abs(k - nxt_back), nxt_back))
            visit[nxt_back] = time + 1

    if now < k:
        nxt_forward = now + 1
        if visit[nxt_forward] < 0 or visit[nxt_forward] > time + 1:
            heappush(q, (time + 1, abs(k - nxt_forward), nxt_forward))
            visit[nxt_forward] = time + 1

        nxt_jump = 2 * now
        if visit[nxt_jump] < 0 or visit[nxt_jump] > time:
            heappush(q, (time, abs(k - nxt_jump), nxt_jump))
            visit[nxt_jump] = time