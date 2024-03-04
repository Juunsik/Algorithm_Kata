# 짝수 홀수 개수


def solution(num_list):
    answer = sum(1 for i in num_list if i % 2 == 0)
    return [answer, len(num_list) - answer]
