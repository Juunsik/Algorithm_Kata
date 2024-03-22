# 수박수박수박수박수박수?

# https://school.programmers.co.kr/learn/courses/30/lessons/12922


def solution(n):
    answer = "수박"
    if n % 2:
        answer *= n // 2 + 1
        return answer[:-1]
    else:
        answer *= n // 2
        return answer
