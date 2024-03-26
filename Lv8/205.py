# 문자 개수 세기

# https://school.programmers.co.kr/learn/courses/30/lessons/181902


def solution(my_string):
    answer = [0] * 52
    for i in my_string:
        if i.isupper():
            answer[ord(i) - 65] += 1
        else:
            answer[ord(i) - 71] += 1
    return answer
