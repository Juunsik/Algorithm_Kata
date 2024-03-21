# 1로 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/181880


def solution(num_list):
    answer = 0
    for i in num_list:
        if i == 1:
            continue
        elif i == 2:
            answer += 1
        else:
            div = 2
            while True:
                if 2**div > i:
                    answer += div - 1
                    break
                div += 1
    return answer
