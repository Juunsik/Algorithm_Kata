# 외계어 사전

# https://school.programmers.co.kr/learn/courses/30/lessons/120869


def solution(spell, dic):
    answer = 0
    for i in dic:
        if len(spell) == len(i):
            cnt = 0
            for j in spell:
                if i.count(j) != 1:
                    continue
                else:
                    cnt += 1
            if cnt == len(spell):
                return 1
    return 2
