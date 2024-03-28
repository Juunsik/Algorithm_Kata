# 그림 확대

# https://school.programmers.co.kr/learn/courses/30/lessons/181836


def solution(picture, k):
    answer = []
    for i in picture:
        line = ""
        for j in i:
            line += j * k
        for _ in range(k):
            answer.append(line)

    return answer
