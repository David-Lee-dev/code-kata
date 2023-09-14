# 숫자 카드 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/135807


from math import gcd


def get_cd(target):
    cd = []
    for i in range(1, target // 2):
        if target % i == 0:
            if i**2 == target:
                cd.append(i)
                continue
            cd.append(i)
            cd.append(target // i)

    return cd


def check_all_pass(arr, n):
    for a in arr:
        if a % n != 0:
            return False
    return True


def check_all_fail(arr, n):
    for a in arr:
        if a % n == 0:
            return False
    return True


def get_result(target, compare):
    cd = get_cd(min(target))
    cd.sort(reverse=True)
    for el in cd:
        if el == 1:
            return 0

        if check_all_pass(target, el) and check_all_fail(compare, el):
            return el
    return 0


def solution(arrayA, arrayB):
    arrayA.sort()
    arrayB.sort()
    answer = max(get_result(arrayA, arrayB), get_result(arrayB, arrayA))
    return answer
