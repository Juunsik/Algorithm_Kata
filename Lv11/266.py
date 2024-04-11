# 코드 처리하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181932


def solution(code):
    answer = ""
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                mode = 1
            elif i % 2 == 0:
                answer += code[i]
        elif mode == 1:
            if code[i] == "1":
                mode = 0
            elif i % 2 == 1:
                answer += code[i]
    return answer if answer else "EMPTY"
