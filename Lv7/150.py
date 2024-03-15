# 등차수열의 특정한 항만 더하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181931


def solution(a, d, included):
    answer = 0
    ap = [a + d * i for i in range(len(included))]
    for i in range(len(included)):
        if included[i]:
            answer += ap[i]
    return answer
