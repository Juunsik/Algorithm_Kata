# 구명보트

# https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        answer += 1
        right -= 1

    return answer
