# x 사이의 개수

# https://school.programmers.co.kr/learn/courses/30/lessons/181867


def solution(myString):
    answer = myString.split("x")
    answer = list(map(len, answer))
    return answer
