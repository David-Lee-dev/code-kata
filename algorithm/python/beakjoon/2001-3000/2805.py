# 2805
#https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

start, end = 1, max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for t in trees:
        if t > mid:
            total += t - mid
        else:
            break

    if total < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)
