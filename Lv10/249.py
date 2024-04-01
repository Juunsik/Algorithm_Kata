# 등수 매기기

# https://school.programmers.co.kr/learn/courses/30/lessons/120882


def solution(score):
    avg = [sum(i) / 2 for i in score]
    avg_sort = sorted(avg, reverse=True)
    answer = []

    for i in avg:
        answer.append(avg_sort.index(i) + 1)

    return answer
