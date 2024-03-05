# 모음 제거


def solution(my_string):
    vowel = ["a", "e", "i", "o", "u"]
    answer = my_string[:]

    for i in my_string:
        if i in vowel:
            answer = answer.replace(i, "")

    return answer
