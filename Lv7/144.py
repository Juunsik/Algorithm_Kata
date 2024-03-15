# 문자열 내 p와 y의 개수

# https://school.programmers.co.kr/learn/courses/30/lessons/12916


def solution(s):
    s = s.lower()
    p_cnt = s.count("p")
    y_cnt = s.count("y")

    if p_cnt == y_cnt:
        return True
    else:
        return False
