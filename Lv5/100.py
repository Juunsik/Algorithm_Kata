# 주사위 게임 1

# https://school.programmers.co.kr/learn/courses/30/lessons/181839


def solution(a, b):
    if a % 2 and b % 2:
        answer = a**2 + b**2
    elif a % 2 or b % 2:
        answer = 2 * (a + b)
    else:
        answer = abs(a - b)
    return answer
