# 시소 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/152996


def get_candis(num):
    delta_mul = [4 / 3, 3 / 2, 2]

    result = []
    for x in delta_mul:
        tmp = num * x

        if int(tmp) == tmp and 100 <= tmp <= 1000:
            result.append(int(tmp))

    return result


def solution(weights):
    answer = 0
    nums = [0] * 1001

    for w in weights:
        nums[w] += 1

    weights = list(set(weights))
    weights.sort()

    for w in weights:
        answer += (nums[w] * (nums[w] - 1)) // 2

        candis = get_candis(w)
        for c in candis:
            if nums[c] > 0:
                answer += nums[w] * nums[c]

    return answer
