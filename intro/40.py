# 숨어있는 숫자의 덧셈(1)


def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer
