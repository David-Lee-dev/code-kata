# 명예의 전당 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3

import heapq

def solution(k, score):
    pq = []
    answer = []
    
    for num in score:
        heapq.heappush(pq, num)
        
        if len(pq) > k:
            heapq.heappop(pq)
            
        answer.append(pq[0])
            
    return answer
