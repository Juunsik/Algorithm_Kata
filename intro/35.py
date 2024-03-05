# 순서쌍의 개수


def solution(n):
    root_num = 0
    answer = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n**0.5 == i:
                root_num += 1
            else:
                answer += 1
    return 2 * answer + root_num
