# 20936
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AY9QUhl6cfQDFAVF&categoryId=AY9QUhl6cfQDFAVF&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

T = int(input())

def find_point(arr):
    for idx in range(len(arr)):
        if idx + 1 != arr[idx]:
            return idx

    return len(arr)

for _ in range(T):
    N = int(input())
    box_list = list(map(int, input().split())) + [0]
    move_record = []
    point = find_point(box_list)
    while point < N:
        box_list[N] = box_list[point]
        box_list[point] = 0
        move_record.append(point + 1)

        while point < N:
            nxt_point = box_list.index(point + 1)
            box_list[point] = box_list[nxt_point]
            box_list[nxt_point] = 0
            point = nxt_point
            move_record.append(point + 1)

        point = find_point(box_list)

    print(len(move_record))
    for r in move_record:
        print(r, end=" ")
    print()