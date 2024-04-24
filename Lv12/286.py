# 귤 고르기

# https://school.programmers.co.kr/learn/courses/30/lessons/138476


def solution(k, tangerine):
    answer = 0
    element = [0] * max(tangerine)
    for i in tangerine:
        element[i - 1] += 1

    element.sort(reverse=True)
    for i in element:
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer
