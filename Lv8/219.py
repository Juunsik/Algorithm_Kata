# 삼각형의 완성조건(2)

# https://school.programmers.co.kr/learn/courses/30/lessons/120868


def solution(sides):
    answer = 0
    long = max(sides)
    short = min(sides)
    for i in range(long - short, long + 1):
        if i + short > long:
            answer += 1
    for i in range(long + 1, long + short + 1):
        if long + short > i:
            answer += 1
    return answer
