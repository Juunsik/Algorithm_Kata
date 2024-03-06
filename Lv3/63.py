# 더 크게 합치기

# https://school.programmers.co.kr/learn/courses/30/lessons/181939


def solution(a, b):
    aob = int(str(a) + str(b))
    boa = int(str(b) + str(a))

    return max(aob, boa)
