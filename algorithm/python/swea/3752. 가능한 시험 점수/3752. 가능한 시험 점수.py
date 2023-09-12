# 3752. 가능한 시험 점수
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do


import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split(' ')))
    arr = [0] * (sum(nums) + 1)
    arr[0] = 1

    for n in nums:
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                arr[i + n] = 1

    result = 0
    for e in arr:
        if e > 0:
            result += 1

    print(f'#{test_case} {result}')
