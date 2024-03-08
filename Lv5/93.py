# 문자열 바꿔서 찾기

# https://school.programmers.co.kr/learn/courses/30/lessons/181864


def solution(myString, pat):
    temp = ""
    for i in myString:
        if i == "A":
            temp += "B"
        elif i == "B":
            temp += "A"
    return 1 if pat in temp else 0
