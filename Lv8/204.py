# 부족한 금액 계산하기

# https://school.programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):
    required = price * count * (count + 1) // 2

    return required - money if money < required else 0
