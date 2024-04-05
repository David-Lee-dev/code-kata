# 1967
# https://www.acmicpc.net/problem/1967

from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

n = int(input())
read_split = lambda: map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    n1, n2, cost = read_split()
    graph[n1].append((n2, cost))
    graph[n2].append((n1, cost))


def find_longest_distance(graph, visit, start, total):
    visit[start] = True

    if total > 0 and len(graph[start]) == 1:
        return start, total

    result = [0, 0]
    for nxt in graph[start]:
        if visit[nxt[0]]:
            continue

        longest_from_node, cost = find_longest_distance(graph, visit, nxt[0], total + nxt[1])
        if result[1] < cost:
            result[0] = longest_from_node
            result[1] = cost

    return result

visit = [False] * (n + 1)
longest_from_root, cost = find_longest_distance(graph, visit, 1, 0)

visit = [False] * (n + 1)
print(find_longest_distance(graph, visit, longest_from_root, 0)[1])
