# 외계행성의 나이

# https://school.programmers.co.kr/learn/courses/30/lessons/120834


def solution(age):
    num_dict = {}
    answer = ""
    for i in range(10):
        num_dict[str(i)] = ord("a") + i

    for i in str(age):
        answer += chr(num_dict[i])
    return answer
