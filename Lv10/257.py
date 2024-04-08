# 피보나치 수

# https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    num_list = [0, 1]
    for i in range(2, n + 1):
        num_list.append(num_list[-1] + num_list[-2])
    return num_list[-1] % 1234567
