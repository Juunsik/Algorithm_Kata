# 숨어있는 숫자의 덧셈(2)

# https://school.programmers.co.kr/learn/courses/30/lessons/120864


def solution(my_string):
    num_str = ""
    for i in my_string:
        if i.isalpha():
            num_str += " "
        else:
            num_str += i

    return sum(int(i) for i in num_str.split())
