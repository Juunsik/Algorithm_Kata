# 문자열 내 마음대로 정렬하기

# https://school.programmers.co.kr/learn/courses/30/lessons/12915


def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer
