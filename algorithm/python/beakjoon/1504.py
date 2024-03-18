# 1504
# https://www.acmicpc.net/problem/1504

from sys import stdin
import heapq

n, e = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
max_value = int(1e9)

for _ in range(e):
    s, e, c = map(int, stdin.readline().split())
    graph[s].append((c, e))
    graph[e].append((c, s))

v1, v2 = map(int, stdin.readline().split())

def dikstra(start):
    # 큐의 원소 = (현재 노드까지의 비용, 노드 번호)
    q = [(0, start)]
    # start에서 다른 노드로 가는데 드는 비용 테이블
    dist_table = [max_value] * (n + 1)

    while q:
        # 가장 가까운 노드
        cost, node = heapq.heappop(q)
        # 현재까지 계산된 비용이 계산된 테이블의 비용보다 작을 경우 업데이트
        # 직행이 아닌 거리가 직행 거리보다 적은 비용이 필요할 수 있으므로
        if cost < dist_table[node]:
            dist_table[node] = cost

        # 현재 노드에서 직행으로 갈 수 있는 노드 탐색
        for linked_node in graph[node]:
            nxt_cost, nxt_node = linked_node
            # start에서 node까지의 비용 + node에서 nxt_node까지의 비용 = start에서 nxt_node까지의 비용
            total_cost = dist_table[node] + nxt_cost
            if total_cost < dist_table[nxt_node]:
                dist_table[nxt_node] = total_cost
                heapq.heappush(q, (total_cost, nxt_node))

    return dist_table


start_node_table = dikstra(1)
v1_node_table = dikstra(v1)
v2_node_table = dikstra(v2)

# print(start_node_table)
# print(v1_node_table)
# print(v2_node_table)

result = min(start_node_table[v1] + v1_node_table[v2] + v2_node_table[n], start_node_table[v2] + v2_node_table[v1] + v1_node_table[n])
if result >= max_value:
    result = -1

print(result)