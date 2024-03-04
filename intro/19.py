# 점의 위치 구하기


def solution(dot):
    return (1 if dot[0] > 0 else 3) if dot[0] * dot[1] > 0 else (4 if dot[0] > 0 else 2)
