# 시저 암호

# https://school.programmers.co.kr/learn/courses/30/lessons/12926


def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += " "
        elif i.isupper():
            if ord(i) + n > ord("Z"):
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        else:
            if ord(i) + n > ord("z"):
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)

    return answer
