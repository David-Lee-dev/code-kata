# 1251.하나로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV15StKqAQkCFAYD&categoryId=AV15StKqAQkCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=2


import sys
import heapq
sys.stdin = open("input.txt", "r")

T = int(input())

class Island:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx


def calc_distance(node1, node2):
    x = abs(node1.x - node2.x)
    y = abs(node1.y - node2.y)

    return (x ** 2) + (y ** 2)


for test_case in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split(' ')))
    y_list = list(map(int, input().split(' ')))
    nodes = []

    for i in range(N):
        x, y = x_list[i], y_list[i]
        nodes.append(Island(x, y, i))

    E = float(input())
    visit = [False] * N
    q = [(0, 0)]
    distance_list = []
    count = 0

    while q and count < N:
        dist, idx = heapq.heappop(q)
        now = nodes[idx]
        if not visit[now.idx]:
            visit[now.idx] = True
            distance_list.append(dist)
            count += 1
        for i in range(N):
            if visit[i]:
                continue

            heapq.heappush(q, (calc_distance(now, nodes[i]), i))

    result = 0
    for d in distance_list:
        result += E * d

    print(f'#{test_case} {round(result)}')