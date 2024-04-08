# 저주의 숫자 3

# https://school.programmers.co.kr/learn/courses/30/lessons/120871


def solution(n):
    answer = 0

    for i in range(n):
        while "3" in str(answer) or answer % 3 == 0:
            answer += 1
        answer += 1
    return answer - 1
