# 부분 문자열 이어 붙여 문자열 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/181911


def solution(my_strings, parts):
    answer = ""
    for i in range(len(parts)):
        answer += my_strings[i][parts[i][0] : parts[i][1] + 1]
    return answer
