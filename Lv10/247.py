# 크기가 작은 부분 문자열

# https://school.programmers.co.kr/learn/courses/30/lessons/147355


def solution(t, p):
    answer = 0
    length = len(p)
    for i in range(len(t) - length + 1):
        if int(t[i : i + length]) <= int(p):
            answer += 1
    return answer
