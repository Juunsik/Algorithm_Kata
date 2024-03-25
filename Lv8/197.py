# qr code

# https://school.programmers.co.kr/learn/courses/30/lessons/181903


def solution(q, r, code):
    answer = ""
    for i, v in enumerate(code):
        if i % q == r:
            answer += v
    return answer
