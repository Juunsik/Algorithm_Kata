# 올바른 괄호

# https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    stk = []

    for i in s:
        if i != ")":
            stk.append(1)
        else:
            if stk:
                stk.pop()
            else:
                return False
    return False if stk else True
