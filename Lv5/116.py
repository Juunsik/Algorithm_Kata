# 인덱스 바꾸기

# https://school.programmers.co.kr/learn/courses/30/lessons/120895


def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return "".join(my_string)
