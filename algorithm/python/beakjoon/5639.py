# 5639
# https://www.acmicpc.net/problem/5639

from sys import stdin, setrecursionlimit
setrecursionlimit(10001)

preorder_arr = []
while True:
    try:
        preorder_arr.append(int(stdin.readline().rstrip()))
    except:
        break

def solution(arr):
    root = arr[0]
    size = len(arr)

    if size == 1:
        print(root)
        return

    idx = 1
    while idx < size and arr[idx] < root:
        idx += 1

    left = arr[1:idx]
    right = arr[idx:]

    if len(left) > 0:
        solution(left)
    if len(right) > 0:
        solution(right)

    print(root)

solution(preorder_arr)