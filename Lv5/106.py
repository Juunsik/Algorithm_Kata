# 홀수 vs 짝수

# https://school.programmers.co.kr/learn/courses/30/lessons/181887


def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
