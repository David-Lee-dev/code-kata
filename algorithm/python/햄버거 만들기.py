# 햄버거 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/133502?language=python3

def solution(ingredient):
    s = []
    cnt = 0
    
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4):
                s.pop()
    return cnt