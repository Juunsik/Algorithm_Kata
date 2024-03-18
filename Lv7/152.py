# 두 정수 사이의 합

# https://school.programmers.co.kr/learn/courses/30/lessons/12912


def solution(a, b):
    answer = 0
    if a == b:
        return a
    for i in range(min(a, b), max(a, b) + 1):
        answer += i
    return answer
