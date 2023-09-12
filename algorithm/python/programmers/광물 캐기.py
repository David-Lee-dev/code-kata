# 광물 캐기
# https://school.programmers.co.kr/learn/courses/30/lessons/172927

from collections import deque

PICKS = ['diamond', 'iron', 'stone']

def calc_fatigue(pick, mineral):
    fatigue_table = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]

    index_table = {
        'diamond': 0,
        'iron': 1,
        'stone': 2
    }

    return fatigue_table[index_table[pick]][index_table[mineral]]


def solution(picks, minerals):
    answer = 0

    minerals = minerals[:sum(picks) * 5]
    mineral_data = []
    pick_spread = deque([])

    for i in range(3):
        for j in range(picks[i]):
            pick_spread.appendleft(PICKS[i])

    while minerals:
        tmp_arr = minerals[:5]
        tmp_dict = { 'diamond': 0, 'iron': 0, 'stone': 0 }

        for el in tmp_arr:
            tmp_dict[el] += 1

        mineral_data.append(tmp_dict)
        minerals = minerals[5:]

    mineral_data.sort(key=lambda x:(-x['diamond'], -x['iron'], -x['stone']))

    for data in mineral_data:
        if not pick_spread:
            break
        pick = pick_spread.pop()

        for mineral in data:
            answer += calc_fatigue(pick, mineral) * data[mineral]

    return answer
