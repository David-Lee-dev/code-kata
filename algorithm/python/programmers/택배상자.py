# 택배상자
# https://school.programmers.co.kr/learn/courses/30/lessons/131704#


def solution(order):
    order.reverse()
    answer = 0
    sub = []

    idx = 1
    while order:
        now = order.pop()

        if now == idx:
            answer += 1
            idx += 1
        elif now > idx:
            while now > idx:
                sub.append(idx)
                idx += 1
            idx += 1
            answer += 1
        else:
            if sub and sub[-1] == now:
            if sub and sub[-1] == now:
                sub.pop()
                answer += 1
            elif now in sub:
                return answer
        # print(now, sub, idx)

    return answer