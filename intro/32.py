# 삼각형의 완성조건(1)


def solution(sides):
    long = max(sides)
    sides.remove(long)
    return 1 if sum(sides) > long else 2
