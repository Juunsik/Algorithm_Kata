# 이진 변환 반복하기

# https://school.programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    answer = [0, 0]
    zero = 0
    cnt = 0
    while s != "1":
        answer[0] += 1
        answer[1] += s.count("0")
        s = format(s.count("1"), "b")
    return answer
