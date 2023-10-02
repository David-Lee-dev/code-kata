# 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502


from collections import deque


def solution(s):
    answer = 0

    s = deque(list(s))
    s_len = len(s)
    for i in range(1, s_len):
        stack = []

        for j in range(s_len):
            if not stack:
                stack.append(s[j])
                continue

            if s[j] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[j] == '}' and stack[-1] == '{':
                stack.pop()
            elif s[j] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[j])

        if not stack:
            answer += 1

        s.append(s.popleft())
    return answer