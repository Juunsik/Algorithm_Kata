# 명예의 전당(1)

# https://school.programmers.co.kr/learn/courses/30/lessons/138477


def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank.sort(reverse=True)
        if len(rank) < k:
            answer.append(rank[-1])
        else:
            answer.append(rank[k - 1])
    return answer
