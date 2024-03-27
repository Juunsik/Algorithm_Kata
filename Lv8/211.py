# 영어가 싫어요

# https://school.programmers.co.kr/learn/courses/30/lessons/120894


def solution(numbers):
    answer = ""
    num_string = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }

    for k, v in num_string.items():
        numbers = numbers.replace(k, v)
    return int(numbers)
