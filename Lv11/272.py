# [1차] 비밀지도

# https://school.programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line = ""
        for _ in range(n):
            arr1_remain = arr1[i] % 2
            arr2_remain = arr2[i] % 2
            line += "#" if (arr1_remain or arr2_remain) else " "
            arr1[i] //= 2
            arr2[i] //= 2
        answer.append(line[::-1])
    return answer
