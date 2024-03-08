# 개미 군단

# https://school.programmers.co.kr/learn/courses/30/lessons/120837


def solution(hp):
    answer = 0
    for i in range(5, 0, -2):
        answer += hp // i
        hp %= i
    return answer
