# 문자열 밀기

# https://school.programmers.co.kr/learn/courses/30/lessons/120921


def solution(A, B):
    for i in range(len(A) + 1):
        if B == A[-i:] + A[:-i]:
            return i
    return -1
