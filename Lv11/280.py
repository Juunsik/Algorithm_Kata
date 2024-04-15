# N개의 최소공배수

# https://school.programmers.co.kr/learn/courses/30/lessons/12953


def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i


def solution(arr):
    while len(arr) > 1:
        lcm_num = lcm(arr[0], arr[1])
        arr = arr[2:] + [lcm_num]
    return arr[0]
