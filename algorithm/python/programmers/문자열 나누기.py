# 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    left_stack = []
    right_stack = []
    
    for w in s:
        left_stack.append(w) if not left_stack or left_stack[-1] == w else right_stack.append(w)
            
        if len(left_stack) == len(right_stack):
            answer += 1
            left_stack = []
            right_stack = []
    
    return answer + (len(left_stack) > 0)