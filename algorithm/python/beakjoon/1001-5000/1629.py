# 1629
# https://www.acmicpc.net/problem/1629

import sys
a, b, c = map(int, sys.stdin.readline().split())
def DaC(a, b):
    if b == 1:
        return a % c

    k = DaC(a, b//2)

    if b % 2 == 0:
        return (k * k) % c
    else:
        return (k * k * a) % c

print(DaC(a,b))