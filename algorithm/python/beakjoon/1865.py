# 1865
# https://www.acmicpc.net/problem/1865

from sys import stdin


def bellman_ford(graph, start, N):
    dist = [5000 * 10000] * (N + 1)
    dist[start] = 0
    for i in range(N):
        for s, e, t in graph:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t

    for s, e, t in graph:
        if dist[e] > dist[s] + t:
            return True


    return False


tc = int(stdin.readline())
for _ in range(tc):
    n, m, w = map(int, stdin.readline().split())
    graph = []

    for _ in range(m):
        s, e, t = map(int, stdin.readline().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, stdin.readline().split())
        graph.append((s, e, -t))

    # for start in range(1, n + 1):
    if bellman_ford(graph, 1, n):
        print('YES')
        # break
    else:
        print('NO')
