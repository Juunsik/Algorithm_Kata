# 특정 문자열로 끝나는 가장 긴 부분

# https://school.programmers.co.kr/learn/courses/30/lessons/181872


def solution(myString, pat):
    answer = myString.rsplit(pat, 1)[0]
    return answer + pat
