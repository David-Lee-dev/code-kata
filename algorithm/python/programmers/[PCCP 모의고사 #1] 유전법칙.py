# [PCCP 모의고사 #1] 유전법칙
# https://school.programmers.co.kr/learn/courses/15008/lessons/121685


def solution(queries):
    answer = []

    for q in queries:
        gene, pos = q
        stack = []

        pos -= 1
        while gene > 1:
            stack.append(pos % 4)
            gene -= 1
            pos //= 4

            print(stack)

        while stack:
            tmp = stack.pop()
            if tmp == 0:
                answer.append("RR")
                break
            if tmp == 3:
                answer.append("rr")
                break
        else:
            answer.append("Rr")

    return answer
