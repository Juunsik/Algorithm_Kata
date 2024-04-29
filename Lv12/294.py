# 2016년

# https://school.programmers.co.kr/learn/courses/30/lessons/12901


def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = {1: "FRI", 2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED", 0: "THU"}
    answer = week[(sum(month[:a]) + b) % 7]
    return answer
