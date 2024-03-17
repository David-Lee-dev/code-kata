# 1238
# https://www.acmicpc.net/problem/1238
import heapq
import pprint
from sys import stdin

class Node:
    def __init__(self):
        self.link = []


n, m, v = map(int, stdin.readline().split())
graph_to_party = [Node() for _ in range(n + 1)]
graph_to_home = [Node() for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, stdin.readline().split())
    graph_to_party[e].link.append((s, c))
    graph_to_home[s].link.append((e, c))


def dikstra(start, graph):
    queue = []
    heapq.heappush(queue, (0, start))
    dist_arr = [100 * n] * (n + 1)
    while queue:
        dist, node = heapq.heappop(queue)
        if dist < dist_arr[node]:
            dist_arr[node] = dist

        for l in graph[node].link:
            dist_sum = dist_arr[node] + l[1]
            if dist_sum < dist_arr[l[0]]:
                dist_arr[l[0]] = dist_sum
                heapq.heappush(queue, (dist_sum, l[0]))

    return dist_arr


a = dikstra(v, graph_to_party)
b = dikstra(v, graph_to_home)

result = 0
for i in range(1, n + 1):
    if i == v:
        continue
    result = max(result, a[i] + b[i])

print(result)