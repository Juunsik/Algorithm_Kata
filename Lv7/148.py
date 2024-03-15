# 하샤드 수

# https://school.programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    div_num = sum(map(int, str(x)))
    if x % div_num == 0:
        return True
    return False
