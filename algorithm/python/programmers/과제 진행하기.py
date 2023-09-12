# 과제 진행하기
# https://school.programmers.co.kr/learn/courses/30/lessons/176962

SUBJECT = 0
START_TIME = 1
PLAY_TIME = 2


def get_minutes(time):
    return int(time[:2]) * 60 + int(time[3:])


def solution(plans):
    answer = []
    q = []
    plans.sort(key=lambda x: get_minutes(x[1]), reverse=True)
    plans = [[plan[0], get_minutes(plan[1]), int(plan[2])] for plan in plans]

    while plans:
        nxt = plans.pop()

        if not q:
            q.append(nxt)
            continue

        if q[-1][START_TIME] + q[-1][PLAY_TIME] > nxt[START_TIME]:
            for idx in range(len(q) - 1, -1, -1):
                q[idx][PLAY_TIME] = q[idx][PLAY_TIME] - (
                    nxt[START_TIME] - q[idx][START_TIME]
                )
                q[idx][START_TIME] = nxt[START_TIME] + nxt[PLAY_TIME]
            q.append(nxt)
        else:
            plans.append(nxt)
            answer.append(q.pop()[SUBJECT])

    while q:
        answer.append(q.pop()[SUBJECT])

    return answer
