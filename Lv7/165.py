# 수열과 구간 쿼리 3

# https://school.programmers.co.kr/learn/courses/30/lessons/181924


def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr
