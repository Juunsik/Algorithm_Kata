# 세로 읽기

# https://school.programmers.co.kr/learn/courses/30/lessons/181904


def solution(my_string, m, c):
    answer = ""
    table = []
    for i in range(0, len(my_string), m):
        table.append(my_string[i : i + m])
    for i in table:
        answer += i[c - 1]
    return answer
