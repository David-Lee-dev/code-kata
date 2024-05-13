# 1043
# https://www.acmicpc.net/problem/1043

from sys import stdin
from collections import deque
class Person:
    def __init__(self):
        self.link = set()


def check_party(party, only_truth):
    for p in party:
        if p in only_truth:
            return False

    return True


n, m = map(int, stdin.readline().split())
relation_table = [Person() for _ in range(n + 1)]
know_true = list(map(int, stdin.readline().split()))[1:]
parties = [list(map(int, stdin.readline().split()))[1:] for _ in range(m)]

for party in parties:
    for i in party:
        one_self = relation_table[i]
        for j in party:
            if i == j:
                continue

            another = relation_table[j]
            one_self.link.add(j)
            another.link.add(i)


only_truth = set()
visited = [False] * (n + 1)

for k in know_true:
    queue = deque([k])
    visited[k] = True
    only_truth.add(k)
    while queue:
        now = queue.popleft()

        for nxt in list(relation_table[now].link):
            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append(nxt)
            only_truth.add(nxt)

result = 0
for party in parties:
    if check_party(party, only_truth):
        result += 1

print(result)