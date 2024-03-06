# 조건에 맞게 수열 변환하기 3

# https://school.programmers.co.kr/learn/courses/30/lessons/181835


def solution(arr, k):
    if k % 2:
        return [i * k for i in arr]
    else:
        return [i + k for i in arr]
