# 3진법 뒤집기

# https://school.programmers.co.kr/learn/courses/30/lessons/68935


def solution(n):
    answer = ""
    while n != 0:
        answer += str(n % 3)
        n //= 3
    print(answer)
    return int(answer, 3)
