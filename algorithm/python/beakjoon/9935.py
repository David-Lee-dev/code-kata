# 9935
# https://www.acmicpc.net/problem/9935

from sys import stdin

def check(arr, string, size):
    for i in range(size):
        if arr[-size + i] != string[i]:
            return False
    return True

string = input()
bomb = input()
bomb_size = len(bomb)

stack = []
stack_size = 0
for w in string:
    stack.append(w)
    stack_size += 1
    if stack_size >= bomb_size and check(stack, bomb, bomb_size):
        for _ in range(bomb_size):
            stack.pop()
        stack_size -= bomb_size

result = ''.join(stack)

print(result if result else 'FRULA')
