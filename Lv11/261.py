# 특이한 정렬

# https://school.programmers.co.kr/learn/courses/30/lessons/120880


def solution(numlist, n):
    answer = []
    minus = [abs(i - n) for i in numlist]
    answer = list(zip(numlist, minus))
    answer.sort(key=lambda x: (x[1], -x[0]))
    answer = [i[0] for i in answer]

    return answer
