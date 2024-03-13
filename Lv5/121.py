# 간단한 식 계산하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181865


def solution(binomial):
    binomial = binomial.split()
    if binomial[1] == "+":
        return int(binomial[0]) + int(binomial[2])
    if binomial[1] == "-":
        return int(binomial[0]) - int(binomial[2])
    if binomial[1] == "*":
        return int(binomial[0]) * int(binomial[2])
