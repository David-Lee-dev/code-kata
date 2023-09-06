# 연속된 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/178870#


def solution(sequence, k):
    candi = []
    left = 0
    right = 0
    while left < len(sequence) and right < len(sequence):
        if left == right:
            summary = sequence[left]

        if summary < k:
            right += 1

            if right == len(sequence):
                break

            summary += sequence[right]
        else:
            if summary == k:
                candi.append([left, right])

            if left == right:
                left = right = left + 1
                continue

            summary -= sequence[left]
            left += 1

    candi.sort(key=lambda e: (e[1] - e[0], e[0]))

    return candi[0]
