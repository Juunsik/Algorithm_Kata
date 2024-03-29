# 최솟값 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/12941


def solution(A, B):
    answer = 0
    a = sorted(A)
    b = sorted(B, reverse=True)

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer
