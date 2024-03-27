# 구슬을 나누는 경우의 수

# https://school.programmers.co.kr/learn/courses/30/lessons/120840


def solution(balls, share):
    up = 1
    down = 1
    for i in range(balls, share, -1):
        up *= i
    for i in range(2, balls - share + 1):
        down *= i

    return up // down
