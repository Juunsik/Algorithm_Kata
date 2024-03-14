# 문자열 정리하기(2)

# https://school.programmers.co.kr/learn/courses/30/lessons/120911


def solution(my_string):
    answer = sorted(my_string.lower())
    return "".join(answer)
