# 두 개 뽑아서 더하기

# https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations


def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        answer.append(sum(i))
    answer = sorted(list(set(answer)))
    return answer
