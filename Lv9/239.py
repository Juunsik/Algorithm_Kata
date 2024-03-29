# 캐릭터의 좌표

# https://school.programmers.co.kr/learn/courses/30/lessons/120861


def solution(keyinput, board):
    answer = [0, 0]
    r = (board[0] - 1) // 2
    l = -r
    u = (board[1] - 1) // 2
    d = -u
    for i in keyinput:
        if i == "up":
            if answer[1] < u:
                answer[1] += 1
        elif i == "right":
            if answer[0] < r:
                answer[0] += 1
        elif i == "down":
            if answer[1] > d:
                answer[1] -= 1
        else:
            if answer[0] > l:
                answer[0] -= 1
    return answer
