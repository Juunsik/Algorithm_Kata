# 암호 해독

# https://school.programmers.co.kr/learn/courses/30/lessons/120892


def solution(cipher, code):
    answer = ""
    for i in cipher[code - 1 :: code]:
        answer += i
    return answer
