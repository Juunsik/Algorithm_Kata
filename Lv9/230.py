# 문자열 겹쳐쓰기

# https://school.programmers.co.kr/learn/courses/30/lessons/181943


def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string) :]
    return answer
