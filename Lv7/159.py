# 빈 배열에 추가, 삭제하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181860


def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            [answer.append(arr[i]) for _ in range(arr[i] * 2)]
        else:
            [answer.pop() for _ in range(arr[i])]
    return answer
