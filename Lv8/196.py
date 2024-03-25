# 커피 심부름

# https://school.programmers.co.kr/learn/courses/30/lessons/181837


def solution(order):
    answer = 0
    for i in order:
        if "americano" in i or "anything" in i:
            answer += 4500
        else:
            answer += 5000
    return answer
