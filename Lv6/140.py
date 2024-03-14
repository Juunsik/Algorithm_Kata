# x만큼 간격이 있는 n개의 숫자

# https://school.programmers.co.kr/learn/courses/30/lessons/12954


def solution(x, n):
    if x > 0:
        answer = [i for i in range(x, x * n + 1, x)]
    elif x < 0:
        answer = [i for i in range(x, x * n - 1, x)]
    else:
        answer = [0 for _ in range(n)]
    return answer
