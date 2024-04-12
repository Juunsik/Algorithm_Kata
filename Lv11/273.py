# 영어 끝말잇기

# https://school.programmers.co.kr/learn/courses/30/lessons/12981


def solution(n, words):
    answer = []

    for i in range(len(words)):
        if words[i] in words[:i] or (i > 0 and words[i][0] != words[i - 1][-1]):
            number = n if (i + 1) % n == 0 else (i + 1) % n
            cycle = (i + 1) // n if number == n else (i + 1) // n + 1
            answer.extend([number, cycle])
            return answer
    return [0, 0]
