# 컨트롤 제트

# https://school.programmers.co.kr/learn/courses/30/lessons/120853


def solution(s):
    s = s.split()
    for i in range(len(s)):
        if s[i] == "Z":
            s[i] = 0
            s[i - 1] = 0
    return sum(list(map(int, s)))
