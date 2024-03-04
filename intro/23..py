# 피자 나눠 먹기(1)


def solution(n):
    answer = n // 7 if n % 7 == 0 else n // 7 + 1
    return answer
