# 두 수의 연산값 비교하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181938


def solution(a, b):
    aob = int(str(a) + str(b))
    cal = 2 * a * b

    return aob if aob >= cal else cal
