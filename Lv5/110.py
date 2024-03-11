# 가까운 1 찾기

# https://school.programmers.co.kr/learn/courses/30/lessons/181898


def solution(arr, idx):
    answer = 0
    for i, v in enumerate(arr):
        if i > idx - 1 and v == 1:
            return i
    return -1
