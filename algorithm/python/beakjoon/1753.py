# 1753
# https://www.acmicpc.net/problem/1753

from sys import stdin
import heapq

INF = -1

v, e = map(int, stdin.readline().split())
k = int(stdin.readline())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    s, e, c = map(int, stdin.readline().split())
    graph[s].append((c, e))

q = [(0, k)]
dist_table = [INF] * (v + 1)
while q:
    cost, node = heapq.heappop(q)

    if dist_table[node] == INF or dist_table[node] > cost:
        dist_table[node] = cost

    for linked_node in graph[node]:
        nxt_cost, nxt_node = linked_node
        if dist_table[nxt_node] == INF or dist_table[nxt_node] > cost + nxt_cost:
            dist_table[nxt_node] = cost + nxt_cost
            heapq.heappush(q, (dist_table[nxt_node], nxt_node))


for i in range(1, v + 1):
    print(dist_table[i] if dist_table[i] >= 0 else 'INF')
