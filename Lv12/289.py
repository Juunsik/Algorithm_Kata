# 카드 뭉치

# https://school.programmers.co.kr/learn/courses/30/lessons/159994


def solution(cards1, cards2, goal):
    cards1.reverse()
    cards2.reverse()
    for i in goal:
        if cards1 and i == cards1[-1]:
            cards1.pop()
        elif cards2 and i == cards2[-1]:
            cards2.pop()
        else:
            return "No"
    return "Yes"
