# 합성수 찾기

# https://school.programmers.co.kr/learn/courses/30/lessons/120846


def solution(n):
    answer = 0
    for i in range(4, n + 1):
        if i % 2 == 0:
            answer += 1
        else:
            div = 0
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    if j**2 == i:
                        div += 1
                    else:
                        div += 2
            if div >= 3:
                answer += 1

    return answer
