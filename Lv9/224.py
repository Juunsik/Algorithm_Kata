# 정사각형으로 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/181830


def solution(arr):
    row = len(arr)
    col = len(arr[0])
    max_rc = max(col, row)
    answer = [[0] * max_rc for _ in range(max_rc)]

    for i in range(row):
        for j in range(col):
            answer[i][j] = arr[i][j]
    return answer
