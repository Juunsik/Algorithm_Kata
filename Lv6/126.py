# 수 조작하기 2

# https://school.programmers.co.kr/learn/courses/30/lessons/181925


def solution(numLog):
    answer = ""
    for i in range(len(numLog) - 1, 0, -1):
        num = numLog[i] - numLog[i - 1]
        if num == 1:
            answer += "w"
        elif num == -1:
            answer += "s"
        elif num == 10:
            answer += "d"
        elif num == -10:
            answer += "a"
    return answer[::-1]
