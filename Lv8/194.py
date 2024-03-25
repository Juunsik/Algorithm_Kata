# 약수의 개수와 덧셈

# https://school.programmers.co.kr/learn/courses/30/lessons/77884


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        div_num = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                div_num += 1
                if j**2 != i:
                    div_num += 1

        if div_num % 2:
            answer -= i
        else:
            answer += i

    return answer
