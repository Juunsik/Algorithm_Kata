# JadenCase 문자열 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/12951


def solution(s):
    answer = ""
    check = 0

    for i in s:
        if i == " ":
            answer += " "
            check = 0
        else:
            if check == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            check += 1

    return answer
