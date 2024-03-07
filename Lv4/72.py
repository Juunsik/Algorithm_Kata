# 원하는 문자열 찾기

# https://school.programmers.co.kr/learn/courses/30/lessons/181878


def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0
