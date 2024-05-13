# 11404
# https://www.acmicpc.net/problem/11404

from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, stdin.readline().split())
    graph[s].append((cost, e))

def dikstra(start):
    dist = ['INF'] * (n + 1)
    q = [(0, start)]

    while q:
        cost, node = heapq.heappop(q)

        if dist[node] == 'INF' or dist[node] > cost:
            dist[node] = cost

        if 0 <= dist[node] < cost:
            continue

        for nxt_cost, nxt_node in graph[node]:
            if dist[nxt_node] == 'INF' or cost + nxt_cost < dist[nxt_node]:
                dist[nxt_node] = cost + nxt_cost
                heapq.heappush(q, (dist[nxt_node], nxt_node))

    return dist

for i in range(1, n + 1):
    dist = dikstra(i)
    dist[i] = 0
    for num in dist[1:]:
        print(num if num != 'INF' else 0, end=' ')
    print()