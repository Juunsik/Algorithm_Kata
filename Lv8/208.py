# 문자열 계산하기

# https://school.programmers.co.kr/learn/courses/30/lessons/120902


def solution(my_string):
    string_list = my_string.split()
    answer = int(string_list[0])
    for i in range(1, len(string_list)):
        if string_list[i] == "+":
            answer += int(string_list[i + 1])
        if string_list[i] == "-":
            answer -= int(string_list[i + 1])
    return answer
