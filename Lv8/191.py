# 리스트 자르기

# https://school.programmers.co.kr/learn/courses/30/lessons/181897


def solution(n, slicer, num_list):
    if n == 1:
        return num_list[: slicer[1] + 1]
    elif n == 2:
        return num_list[slicer[0] :]
    elif n == 3:
        return num_list[slicer[0] : slicer[1] + 1]
    elif n == 4:
        return num_list[slicer[0] : slicer[1] + 1 : slicer[2]]
    return answer
