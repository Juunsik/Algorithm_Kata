# 내적

# https://school.programmers.co.kr/learn/courses/30/lessons/70128


def solution(a, b):
    answer = sum(a[i] * b[i] for i in range(len(a)))
    return answer
