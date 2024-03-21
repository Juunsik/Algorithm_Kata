# 진료순서 정하기

# https://school.programmers.co.kr/learn/courses/30/lessons/120835


def solution(emergency):
    answer = [0] * len(emergency)

    for i in range(1, len(emergency) + 1):
        answer[emergency.index(max(emergency))] = i
        emergency[emergency.index(max(emergency))] = 0
    return answer
