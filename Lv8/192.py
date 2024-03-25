# 7의 개수

# https://school.programmers.co.kr/learn/courses/30/lessons/120912


def solution(array):
    answer = "".join(map(str, array))
    return answer.count("7")
