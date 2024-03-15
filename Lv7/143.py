# 자연수 뒤집어 배열로 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/12932


def solution(n):
    answer = list(map(int, str(n)))

    return answer[::-1]
