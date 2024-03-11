# l로 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/181834


def solution(myString):
    answer = ""
    for i in myString[:]:
        if i < "l":
            answer += "l"
        else:
            answer += i
    return answer
