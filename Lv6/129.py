# 문자열 잘라서 정렬하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181866


def solution(myString):
    answer = []
    for i in myString.split("x"):
        if i != "":
            answer.append(i)
    return sorted(answer)
