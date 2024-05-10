# 16236
# https://www.acmicpc.net/problem/16236

from sys import stdin
from collections import deque
from heapq import heappush, heappop


directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


class Shark:
    def __init__(self, r, c):
        self.size = 2
        self.need_food = 2
        self.location = (r, c)
        self.time = 0


    def eat(self, food):
        self.need_food -= 1
        self.location = (food[1], food[2])
        self.time += food[0]

        if self.need_food == 0:
            self.size += 1
            self.need_food = self.size

def find_food(matrix, shark):
    visited = [[False] * n for _ in range(n)]
    visited[shark.location[0]][shark.location[1]] = True
    q = deque([(shark.location[0], shark.location[1], 0)])
    candis = []

    while q:
        r, c, t = q.popleft()

        if 0 < matrix[r][c] < shark.size:
            heappush(candis, (t, r, c))

        for d in directions:
            nxt_r = r + d[0]
            nxt_c = c + d[1]

            if not (0 <= nxt_r < n):
                continue
            if not (0 <= nxt_c < n):
                continue
            if visited[nxt_r][nxt_c]:
                continue
            if matrix[nxt_r][nxt_c] > shark.size:
                continue

            q.append((nxt_r, nxt_c, t + 1))
            visited[nxt_r][nxt_c] = True

    if candis:
        return candis[0]


n = int(stdin.readline())
matrix = []
shark = None
for r in range(n):
    matrix.append(list(map(int, stdin.readline().split())))
    for c in range(n):
        if matrix[r][c] == 9:
            shark = Shark(r, c)
            matrix[r][c] = 0


while True:
    nxt_food = find_food(matrix, shark)

    if not nxt_food:
        print(shark.time)
        break

    shark.eat(nxt_food)
    matrix[nxt_food[1]][nxt_food[2]] = 0