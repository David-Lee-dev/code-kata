# 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

score_table = [0, 3, 2, 1, 0, 1, 2, 3]


def solution(survey, choices):
    result_table = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for idx in range(len(survey)):
        survey_type = survey[idx]
        choice_num = choices[idx]

        if choice_num == 4:
            continue

        answer_table = [0] + ([survey_type[0]] * 3) + [0] + ([survey_type[1]] * 3)
        result_table[answer_table[choice_num]] += score_table[choice_num]

    answer = (
        ("R" if result_table["R"] >= result_table["T"] else "T")
        + ("C" if result_table["C"] >= result_table["F"] else "F")
        + ("J" if result_table["J"] >= result_table["M"] else "M")
        + ("A" if result_table["A"] >= result_table["N"] else "N")
    )

    return answer
