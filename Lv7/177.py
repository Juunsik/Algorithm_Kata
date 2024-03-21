# 가까운 수

# https://school.programmers.co.kr/learn/courses/30/lessons/120890


def solution(array, n):
    array.sort()
    closer = abs(n - array[0])
    answer = array[0]
    for i in array[1:]:
        if abs(n - i) < closer:
            closer = abs(n - i)
            answer = i
    return answer
