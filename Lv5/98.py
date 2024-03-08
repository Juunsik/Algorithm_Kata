# A 깅조하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181874


def solution(myString):
    answer = ""
    for i in myString:
        if i == "a" or i == "A":
            answer += "A"
        else:
            answer += i.lower()
    return answer
