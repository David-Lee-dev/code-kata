# 1916
# https://www.acmicpc.net/problem/1916

from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, stdin.readline().split())
    graph[s].append((c, e))
start, end = map(int, stdin.readline().split())
dist_table = [-1] * (n + 1)
q = [(0, start)]
while q:
    cost, node = heapq.heappop(q)
    if 0 <= dist_table[node] < cost:
        continue
    if dist_table[node] == -1 or dist_table[node] > cost:
        dist_table[node] = cost
    for linked_node in graph[node]:
        nxt_cost, nxt_node = linked_node
        if dist_table[nxt_node] == -1 or dist_table[nxt_node] > cost + nxt_cost:
            dist_table[nxt_node] = cost + nxt_cost
            heapq.heappush(q, (dist_table[nxt_node], nxt_node))
print(dist_table[end])

