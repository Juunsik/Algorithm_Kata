# 약수의 합

# https://school.programmers.co.kr/learn/courses/30/lessons/12928


def solution(n):
    answer = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i**2 != n:
                answer += n // i
            answer += i

    return answer
