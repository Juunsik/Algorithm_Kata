# K번째 수

# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for s, e, i in commands:
        temp = array[s - 1 : e]
        temp.sort()
        answer.append(temp[i - 1])
    return answer
