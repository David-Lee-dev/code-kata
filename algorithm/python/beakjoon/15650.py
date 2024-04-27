# 15650
# https://www.acmicpc.net/problem/15650

from sys import stdin
n, m = map(int, stdin.readline().split())

nums = [i for i in range(1, n + 1)]
arr = []

def combination(index, count):
    if count == m:
        print(' '.join(arr))
        return
    if index >= n:
        return

    arr.append(str(nums[index]))
    combination(index + 1, count + 1)
    arr.pop()
    combination(index + 1, count)


combination(0, 0)
