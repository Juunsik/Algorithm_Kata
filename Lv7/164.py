# 콜라츠 추측

# https://school.programmers.co.kr/learn/courses/30/lessons/12943


def solution(num):
    answer = 0
    while num != 1:
        if num % 2:
            num = num * 3 + 1
        else:
            num //= 2
        answer += 1
    return answer if answer <= 500 else -1
