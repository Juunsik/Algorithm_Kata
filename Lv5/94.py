# 5명씩

# https://school.programmers.co.kr/learn/courses/30/lessons/181886


def solution(names):
    answer = []
    for i in range(0, len(names), 5):
        answer.append(names[i])
    return answer
