# 중복된 문자 제거

# https://school.programmers.co.kr/learn/courses/30/lessons/120888


def solution(my_string):
    answer = "".join(dict.fromkeys(my_string))
    return answer
