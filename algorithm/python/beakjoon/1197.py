# 1197
# https://www.acmicpc.net/problem/1197

from sys import stdin
from heapq import heapify, heappush, heappop


v, e = map(int, stdin.readline().split())
links = [tuple(map(int, stdin.readline().split())) for _ in range(e)]
visited = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
for s, d, c in links:
    graph[s].append((c, d))
    graph[d].append((c, s))


result = 0
visited[1] = True
q = graph[1]
heapify(q)

while q:
    cost, dist = heappop(q)

    if not visited[dist]:
        visited[dist] = True
        result += cost

        for edge in graph[dist]:
            if not visited[edge[1]]:
                heappush(q, edge)

print(result)