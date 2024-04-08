# 다음 큰 숫자

# https://school.programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):
    answer = 0
    n_one_num = format(n, "b").count("1")
    n += 1
    while n <= 1000000:
        one_num = format(n, "b").count("1")

        if n_one_num == one_num:
            return n
        n += 1

    return answer
