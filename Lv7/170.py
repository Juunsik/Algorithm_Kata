# k의 개수

# https://school.programmers.co.kr/learn/courses/30/lessons/120887


def solution(i, j, k):
    answer = ""
    for i in range(i, j + 1):
        answer += str(i)
    return answer.count(str(k))
