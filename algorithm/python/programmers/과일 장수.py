# 과일 장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=python3

def solution(k, m, score):
    answer = 0
    count = {}
    for a in score:
        count[str(a)] = count[str(a)] + 1 if count.get(str(a)) else 1
    keys = sorted(list(count.keys()), reverse=True)

    for i in range(len(keys)):
        tmp = count[keys[i]] % m
        count[keys[i]] //= m
        if i == len(keys) - 1:
            break
        count[keys[i + 1]] += tmp
    
    for key, value in count.items():
        answer += int(key) * value * m
        
    return answer

