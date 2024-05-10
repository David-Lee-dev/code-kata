# 1167
# https://www.acmicpc.net/problem/1167

from sys import stdin
from collections import deque

class Node:
    def __init__(self, n):
        self.number = n
        self.link = []


v = int(stdin.readline())
nodes = [0] + [Node(i + 1) for i in range(v)]

for _ in range(1, v + 1):
    data = list(map(int, stdin.readline().split()))

    for j in range(1, len(data) - 1, 2):
        nodes[data[0]].link.append((data[j], data[j + 1]))

cost_table = [-1] * (v + 1)
queue = deque([nodes[1]])
cost_table[1] = 0
max_index = 1

while queue:
    node = queue.popleft()

    for nxt, cost in node.link:
        if cost_table[nxt] >= 0:
            continue

        cost_table[nxt] = cost_table[node.number] + cost
        nxt_node = nodes[nxt]
        queue.append(nxt_node)
        if cost_table[max_index] < cost_table[nxt]:
            max_index = nxt


cost_table = [-1] * (v + 1)
queue = deque([nodes[max_index]])
cost_table[max_index] = 0
result = 0

while queue:
    node = queue.popleft()

    for nxt, cost in node.link:
        if cost_table[nxt] >= 0:
            continue

        cost_table[nxt] = cost_table[node.number] + cost
        nxt_node = nodes[nxt]
        queue.append(nxt_node)
        result = max(result, cost_table[nxt])

print(result)

