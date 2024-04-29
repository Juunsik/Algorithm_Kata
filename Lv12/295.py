# 폰켓몬

# https://school.programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums):
    nums_2 = int(len(nums) / 2)
    nums = list(set(nums))
    if len(nums) < nums_2:
        answer = len(nums)
    else:
        answer = nums_2
    return answer
