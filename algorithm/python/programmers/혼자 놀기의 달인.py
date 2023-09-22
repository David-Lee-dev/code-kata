# 혼자 놀기의 달인
# https://school.programmers.co.kr/learn/courses/30/lessons/131130


def open_box(idx, cards, visit):
    if visit[idx]:
        return 0

    visit[idx] = True

    if cards[idx] == idx + 1:
        return 1
    else:
        return 1 + open_box(cards[idx] - 1, cards, visit)


def solution(cards):
    visit = [False] * len(cards)
    groups = []

    for i, n in enumerate(cards):
        if visit[i]:
            continue
        groups.append(open_box(i, cards, visit))

    groups.sort()

    if len(groups) == 1:
        return 0

    return groups.pop() * groups.pop()