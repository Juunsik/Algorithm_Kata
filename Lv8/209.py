# 배열 만들기 6

# https://school.programmers.co.kr/learn/courses/30/lessons/181859


def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if stk:
            if stk[-1] != arr[i]:
                stk.append(arr[i])
            else:
                stk.pop()
        else:
            stk.append(arr[i])
        i += 1
    return stk if stk else [-1]
