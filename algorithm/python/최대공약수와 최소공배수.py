# 최대공약수와 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12940#


def div_num(target, num):
    cnt = 0
    while target % num == 0:
        cnt += 1
        target //= num

    return cnt, target


def solution(n, m):
    greatest_common_divisor = 1
    least_common_multiple = 1

    i = 2
    while n > 1 or m > 1:
        n_cnt = 0
        m_cnt = 0

        if n > 1 and n >= i:
            n_cnt, n = div_num(n, i)
        if m > 1 and m >= i:
            m_cnt, m = div_num(m, i)

        greatest_common_divisor *= i ** min(n_cnt, m_cnt)
        least_common_multiple *= i ** max(n_cnt, m_cnt)
        i += 1

    return [greatest_common_divisor, least_common_multiple]
