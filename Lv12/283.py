# 최빈값 구하기

# https://school.programmers.co.kr/learn/courses/30/lessons/120812


def solution(array):
    set_a = list(set(array))
    array = {i: array.count(i) for i in set_a}
    answer = [k for k, v in array.items() if max(array.values()) == v]
    if len(answer) > 1:
        return -1
    else:
        return int("".join(map(str, answer)))
