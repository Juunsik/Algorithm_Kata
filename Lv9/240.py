# 직사각형 넓이 구하기

# https://school.programmers.co.kr/learn/courses/30/lessons/120860


def solution(dots):
    dots = sorted(dots, key=lambda x: (x[0], x[1]))
    return abs(dots[-1][0] - dots[0][0]) * abs(dots[-1][1] - dots[0][1])
