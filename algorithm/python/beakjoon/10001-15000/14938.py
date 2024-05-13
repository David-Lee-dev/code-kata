# 14938
# https://www.acmicpc.net/problem/14938

from sys import stdin
from heapq import heappush, heappop

n, m, r = map(int, stdin.readline().split())
items = list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, cost = map(int, stdin.readline().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))


def dijkstra(start):
    q = [(0, start)]
    result = [-1] * (n + 1)

    while q:
        cost, node = heappop(q)

        if result[node] == -1:
            result[node] = cost

        if result[node] < cost:
            continue

        for nxt_node, nxt_cost in graph[node]:
            total_cost = cost + nxt_cost

            if result[nxt_node] == -1 or result[nxt_node] > total_cost:
                result[nxt_node] = total_cost
                heappush(q, (total_cost, nxt_node))
    return result


def calc(result):
    total = 0

    for i in range(1, n + 1):
        if 0 <= result[i] <= m:
            total += items[i - 1]

    return total

max_items = 0
for i in range(1, n + 1):
    result = dijkstra(i)
    max_items = max(max_items, calc(result))

print(max_items)