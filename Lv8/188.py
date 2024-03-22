# 문자열 묶기

# https://school.programmers.co.kr/learn/courses/30/lessons/181855


def solution(strArr):
    answer = list(map(len, strArr))
    cnt = list(set(answer))
    return max([answer.count(i) for i in cnt])
