# 콜라츠 수열 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/181919


def solution(n):
    answer = [n]
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        answer.append(n)

    return answer
