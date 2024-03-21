# 팩토리얼

# https://school.programmers.co.kr/learn/courses/30/lessons/120848


def solution(n):
    answer = 1
    num = 2
    while True:
        answer *= num
        if answer > n:
            return num - 1
        num += 1
