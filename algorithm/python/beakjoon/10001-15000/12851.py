# 12851
# https://www.acmicpc.net/problem/12851

from sys import stdin
from heapq import heappush, heappop

n, k = map(int, stdin.readline().split())
cnt = [None, 0]
visit = [-1] * 200000
q = [(0, abs(k - n), n)]

while q:
    time, _, loc = heappop(q)

    if cnt[0] and cnt[0] < time:
        continue

    if loc == k:
        cnt[0] = time
        cnt[1]+= 1
        continue


    go = loc + 1
    back = loc - 1
    jump = 2 * loc
    nxt_time = time + 1

    if loc < k and (visit[jump] == -1 or visit[jump] >= nxt_time):
        visit[jump] = nxt_time
        heappush(q, (nxt_time, abs(k - jump), jump))
    if loc < k and (visit[go] == -1 or visit[go] >= nxt_time):
        visit[go] = nxt_time
        heappush(q, (nxt_time, abs(k - go), go))
    if back >= 0 and (visit[back] == -1 or visit[back] >= nxt_time):
        visit[back] = nxt_time
        heappush(q, (nxt_time, abs(k - back), back))

print(cnt[0])
print(cnt[1])