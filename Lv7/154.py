# 날짜 비교하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181838

from datetime import datetime


def solution(date1, date2):
    date1 = "".join(map(str, date1))
    date2 = "".join(map(str, date2))

    if int(date1) < int(date2):
        return 1
    return 0
