# 최소직사각형

# https://school.programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    answer = 0
    row = max(sizes[0])
    col = min(sizes[0])
    for i in sizes[1:]:
        row = max(max(i), row)
        col = max(min(i), col)

    return row * col
