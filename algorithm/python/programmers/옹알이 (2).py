# 옹알이 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def count(babbling, before):
    if len(babbling) == 0:
        return 0
    
    if babbling.startswith("aya") and babbling[:3] != before:
        return 1 + count(babbling[3:], babbling[:3])
    elif babbling.startswith("ye") and babbling[:2] != before:
        return 1 + count(babbling[2:], babbling[:2])
    elif babbling.startswith("woo") and babbling[:3] != before:
        return 1 + count(babbling[3:], babbling[:3])
    elif babbling.startswith("ma") and babbling[:2] != before:
        return 1 + count(babbling[2:], babbling[:2])
    else:
        return -100
    
    
def solution(babbling):
    answer = 0
    for b in babbling:
        result = count(b, "")
        if result > 0:
            print(b)
        answer += 0 if result < 0 else 1
    
    return answer