# [PCCP 모의고사 #2] 실습용 로봇
# https://school.programmers.co.kr/learn/courses/15009/lessons/121687?language=python3


delta_x = [0, -1, 0, 1]
delta_y = [1, 0, -1, 0]


def solution(command):
    answer = []
    pos = [0, 0]
    dirc = 0

    def change_dirc(dirc, command):
        if command == "R":
            dirc -= 1
        if command == "L":
            dirc += 1

        if dirc < 0:
            return 3
        if dirc > 3:
            return 0

        return dirc

    for c in command:
        if c in "RL":
            dirc = change_dirc(dirc, c)
            continue

        if c == "G":
            pos[0] += delta_x[dirc]
            pos[1] += delta_y[dirc]
        else:
            pos[0] -= delta_x[dirc]
            pos[1] -= delta_y[dirc]

    return pos
