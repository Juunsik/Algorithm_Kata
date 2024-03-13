# 접미사 배열

# https://school.programmers.co.kr/learn/courses/30/lessons/181909


def solution(my_string):
    answer = [my_string[-i:] for i in range(1, len(my_string) + 1)]
    answer.sort()
    return answer
