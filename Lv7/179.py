# 한 번만 등장한 문자

# https://school.programmers.co.kr/learn/courses/30/lessons/120896


def solution(s):
    answer = []
    ss = list(set(s))
    for i in ss:
        if s.count(i) == 1:
            answer.append(i)
    answer.sort()
    return "".join(answer)
