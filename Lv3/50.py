# 공배수

# https://school.programmers.co.kr/learn/courses/30/lessons/181936


def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0
