# H-Index

# https://school.programmers.co.kr/learn/courses/30/lessons/42747


def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)

    for i in range(n):
        if citations[i] < (i + 1):
            return i
    return n
