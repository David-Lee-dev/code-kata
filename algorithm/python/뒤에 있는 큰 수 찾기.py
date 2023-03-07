```python3
// 뒤에 있는 큰 수 찾기
// https://school.programmers.co.kr/learn/courses/30/lessons/154539?language=python3

def find(idx, numbers, answer, length):
    for i in range(idx + 1, length):        
        tmp = max(numbers[i], answer[i])
        if tmp > numbers[idx]:
            return tmp
        
    return -1
        
        

def solution(numbers):
    length = len(numbers)
    answer = [-1] * length
    peek = numbers[length - 1]
    
    for idx in range(length - 2, -1, -1):
        now = numbers[idx]
        nxt = numbers[idx + 1]
        peek = max(now, peek)
        
        if now < nxt:
            answer[idx] = nxt
            continue
        if now == nxt:
            answer[idx] = answer[idx + 1]
            continue
        if now >= peek:
            answer[idx] = -1
            continue
    
        answer[idx] = find(idx, numbers, answer, length)
    
    return answer
```
