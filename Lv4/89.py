# 첫 번째로 나오는 음수

# https://school.programmers.co.kr/learn/courses/30/lessons/181896


def solution(num_list):
    for i, v in enumerate(num_list):
        if v < 0:
            return i
    return -1
