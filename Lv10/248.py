# 전국 대회 선발 고사

# https://school.programmers.co.kr/learn/courses/30/lessons/181851


def solution(rank, attendance):
    answer = 0
    for i in range(len(attendance)):
        if attendance[i] == False:
            rank[i] = float("inf")

    num = 10000
    for _ in range(3):
        top = rank.index(min(rank))
        answer += num * top

        num = num // 100
        rank[top] = float("inf")

    return answer
