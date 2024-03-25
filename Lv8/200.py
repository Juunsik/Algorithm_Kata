# 조건에 맞게 수열 변환하기 2

# https://school.programmers.co.kr/learn/courses/30/lessons/181881


def solution(arr):
    answer = arr[:]
    cnt = 0
    while True:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        if answer == arr:
            return cnt
        answer = arr[:]
        cnt += 1
