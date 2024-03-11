# 배열의 원소 삭제하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181844


def solution(arr, delete_list):
    answer = []
    for i in arr:
        if i not in delete_list:
            answer.append(i)
    return answer
