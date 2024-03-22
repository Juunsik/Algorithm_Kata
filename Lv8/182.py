# 배열의 길이를 2의 거듭제곱으로 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/181857


def solution(arr):
    power = [2**i for i in range(11)]

    for i in range(1, len(power)):
        if power[i] == len(arr) or len(arr) == 1:
            return arr
        elif power[i] > len(arr):
            arr.extend([0] * (power[i] - len(arr)))
            return arr
