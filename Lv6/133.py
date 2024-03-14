# 피자 나눠 먹기 2

# https://school.programmers.co.kr/learn/courses/30/lessons/120815


def solution(n):

    for i in range(max(n, 6), n * 6 + 1):
        if i % n == 0 and i % 6 == 0:
            return i // 6
