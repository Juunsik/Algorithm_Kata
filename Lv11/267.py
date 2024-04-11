# 숫자 문자열과 영단어

# https://school.programmers.co.kr/learn/courses/30/lessons/81301


def solution(s):
    num_string = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for i in num_string:
        if i in s:
            s = s.replace(i, str(num_string.index(i)))

    answer = int(s)
    return answer
