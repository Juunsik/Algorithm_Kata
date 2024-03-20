# 서울에서 김서방 찾기

# https://school.programmers.co.kr/learn/courses/30/lessons/12919


def solution(seoul):
    for i, v in enumerate(seoul):
        if v == "Kim":
            return f"김서방은 {i}에 있다"
