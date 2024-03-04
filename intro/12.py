# 머쓱이보다 키 큰 사람


def solution(array, height):
    answer = len([i for i in array if height < i])
    return answer
