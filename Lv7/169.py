# A로 B 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/120886


def solution(before, after):
    str_list = list(set(before))
    for i in str_list:
        if before.count(i) != after.count(i):
            return 0
    return 1
