# 추억 점수

# https://school.programmers.co.kr/learn/courses/30/lessons/176963


def solution(name, yearning, photo):
    answer = []
    name = {name[i]: yearning[i] for i in range(len(name))}
    for i in photo:
        result = 0
        for j in i:
            if j in name.keys():
                result += name[j]
        answer.append(result)
    return answer
