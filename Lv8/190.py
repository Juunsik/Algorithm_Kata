# 2의 영역

# https://school.programmers.co.kr/learn/courses/30/lessons/181894


def solution(arr):
    if arr.count(2) == 0:
        return [-1]
    elif arr.count(2) == 1:
        return [2]
    else:
        s = arr.index(2)
        e = len(arr) - arr[::-1].index(2)
        return arr[s:e]
