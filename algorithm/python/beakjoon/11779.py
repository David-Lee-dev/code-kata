# 11779
# https://www.acmicpc.net/problem/11779
import heapq
from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, d, c = map(int, stdin.readline().split(' '))
    graph[s].append((c, d))


def dijkstra(start):
    dist = ['INF'] * (n + 1)
    q = [(0, start)]

    while q:
        cost, node = heapq.heappop(q)

        if dist[node] == 'INF':
            dist[node] = (cost, node)

        if dist[node][0] < cost:
            continue

        for nxt_cost, nxt_node in graph[node]:
            total_cost = cost + nxt_cost
            if dist[nxt_node] == 'INF' or dist[nxt_node][0] > total_cost:
                dist[nxt_node] = (total_cost, node)
                heapq.heappush(q, (total_cost, nxt_node))

    return dist

start, dist = map(int, stdin.readline().split())
result = dijkstra(start)
print(result[dist][0])
path = [dist]
while dist != start:
    dist = result[dist][1]
    path.append(dist)
print(len(path))
for i in range(len(path) - 1, -1, -1):
    print(path[i], end=" ")
