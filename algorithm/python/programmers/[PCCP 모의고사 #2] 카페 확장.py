# [PCCP 모의고사 #2] 카페 확장
# https://school.programmers.co.kr/learn/courses/15009/lessons/121689


def solution(menu, order, k):
    answer = 0

    q = []
    head = 0
    for i, o in enumerate(order):
        cur = k * i
        gst = [k * i, (k * i) + menu[o]]

        pop_list = 0
        if q and q[-1][1] > cur:
            gst[1] += q[-1][1] - cur

        q.append(gst)

        while q[head][1] <= cur:
            head += 1

        answer = max(answer, len(q[head:]))

    return answer
