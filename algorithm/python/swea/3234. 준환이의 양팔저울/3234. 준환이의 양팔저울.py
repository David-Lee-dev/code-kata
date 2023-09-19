def put(idx, left, right, p):
    global N, result, sum_w

    if idx == N:
        result += 1
        return
    if left > sum_w // 2:
        n = N - idx
        result += (2 ** n)
        return

    put(idx + 1, left + p[idx], right, p)
    if right + p[idx] <= left:
        put(idx + 1, left, right + p[idx], p)


def perm(length, now, remaining):
    # 순열이 완성될 때마다 put 함수 호출
    if length == N:
        put(0, 0, 0, now)
        return

    for i in range(len(remaining)):
        perm(length + 1, now + [remaining[i]], remaining[:i] + remaining[i + 1:])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    sum_w = sum(weights)
    result = 0
    perm(0, [], weights)

    print('#{} {}'.format(tc, result))