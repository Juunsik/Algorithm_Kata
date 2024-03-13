# 배열 회전시키기

# https://school.programmers.co.kr/learn/courses/30/lessons/120844


def solution(numbers, direction):
    if direction == "left":
        answer = numbers[1:] + numbers[:1]
    elif direction == "right":
        answer = numbers[-1:] + numbers[:-1]
    return answer
