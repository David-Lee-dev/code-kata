# 할인 행사
# https://school.programmers.co.kr/learn/courses/30/lessons/131127


def solution(want, number, discount):
    answer = 0

    discount_len = len(discount)
    want_len = len(want)

    idx = -1
    dp = [{}] * discount_len
    while idx >= -discount_len:
        dp[idx] = dp[idx + 1].copy()

        if dp[idx].get(discount[idx]):
            dp[idx][discount[idx]] += 1
        else:
            dp[idx][discount[idx]] = 1

        if idx < -10:
            dp[idx][discount[idx + 10]] -= 1

        idx -= 1

    for table in dp:
        for idx in range(want_len):
            if not table.get(want[idx]):
                break
            if table[want[idx]] is not number[idx]:
                break
        else:
            answer += 1

    return answer
