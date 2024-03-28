# 무작위로 k개의 수 뽑기

# https://school.programmers.co.kr/learn/courses/30/lessons/181858


def solution(arr, k):
    answer = list(dict.fromkeys(arr))
    return answer[:k] if len(answer) >= k else answer + [-1] * (k - len(answer))
