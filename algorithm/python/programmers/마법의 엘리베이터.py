# 마법의 엘리베이터
# https://school.programmers.co.kr/learn/courses/30/lessons/148653#qna


from collections import deque


def solution(storey):
    answer = storey

    q = deque([(storey, 0, False)])

    while q:
        now, cnt, flag = q.popleft()

        if now < 10:
            answer = min(cnt + now, answer)
            if not flag:
                q.append((1, cnt + (10 - now), True))
            continue

        tmp = now % 10
        nxt = now // 10

        q.append((nxt, cnt + tmp, flag))
        q.append((nxt + 1, cnt + (10 - tmp), flag))

    return answer
