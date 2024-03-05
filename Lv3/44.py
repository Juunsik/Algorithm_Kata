# 이어 붙인 수

# https://school.programmers.co.kr/learn/courses/30/lessons/181928


def solution(num_list):
    even = ""
    odd = ""
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)

    return int(even) + int(odd)
