# 배열 만들기2

# https://school.programmers.co.kr/learn/courses/30/lessons/181921


def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        s = list(set(str(i)))
        for j in s:
            if j not in ("0", "5"):
                break
        else:
            answer.append(i)
    return answer if answer else [-1]
