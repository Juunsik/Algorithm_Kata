# 유한소수 판별하기

# https://school.programmers.co.kr/learn/courses/30/lessons/120878

def divisor(a, b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return a // i, b // i
    return a, b


def solution(a, b):
    a, b = divisor(a, b)
    if b==1: # 분자값이 더 커서 분모로 나누어 떨어지는 경우
        return 1
    answer = []
    while b > 0:
        for i in range(2, b + 1):
            if b % i == 0:
                answer.append(i)
                break
        b //= i
    answer = list(set(answer))
    return 1 if answer.count(2) + answer.count(5) == len(answer) else 2