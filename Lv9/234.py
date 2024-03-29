# 같은 숫자는 싫어

# https://school.programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    stk = [arr[0]]

    for i in arr:
        if stk[-1] != i:
            stk.append(i)

    return stk
