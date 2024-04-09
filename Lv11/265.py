# 가장 가까운 같은 글자

# https://school.programmers.co.kr/learn/courses/30/lessons/142086


def solution(s):
    answer = []
    idx = {}

    for i in range(len(s)):
        if s[i] not in idx.keys():
            answer.append(-1)
            idx[s[i]] = i
        else:
            answer.append(i - idx[s[i]])
            idx[s[i]] = i
    return answer
