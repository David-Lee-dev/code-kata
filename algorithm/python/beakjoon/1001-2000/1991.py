# 1991
# https://www.acmicpc.net/problem/1991

from sys import stdin

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left if left != '.' else None
        self.right = right if right != '.' else None


table = dict()

n = int(stdin.readline())
for _ in range(n):
    n, l, r = stdin.readline().split()
    table[n] = Node(n, l, r)

forward = []
middle = []
back = []

def trip(name):
    node = table[name]
    forward.append(node.name)

    if node.left:
        trip(node.left)

    middle.append(node.name)

    if node.right:
        trip(node.right)

    back.append(node.name)


trip('A')

print(''.join(forward))
print(''.join(middle))
print(''.join(back))