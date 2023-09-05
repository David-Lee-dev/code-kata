# 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128


def cnt_numbers(string):
    result = dict()

    for w in string:
        if result.get(w):
            result[w] += 1
        else:
            result[w] = 1

    return result


def solution(X, Y):
    x_cnt = cnt_numbers(X)
    y_cnt = cnt_numbers(Y)
    common = dict()

    for key in x_cnt.keys():
        if y_cnt.get(key):
            common[key] = min(x_cnt[key], y_cnt[key])

    result = ""
    for key in [str(i) for i in range(9, -1, -1)]:
        if common.get(key):
            result += key * common[key]

    if not result:
        return "-1"
    elif result[0] == "0":
        return "0"
    return result
