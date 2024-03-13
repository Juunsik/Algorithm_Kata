# 숫자 찾기

# https://school.programmers.co.kr/learn/courses/30/lessons/120904


def solution(num, k):
    if str(k) in str(num):
        return int(str(num).index(str(k))) + 1
    else:
        return -1
