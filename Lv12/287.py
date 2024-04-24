# Ox퀴즈

# https://school.programmers.co.kr/learn/courses/30/lessons/120907


def solution(quiz):
    answer = []
    for cal in quiz:
        cal = cal.split()
        if (cal[1] == "+" and int(cal[0]) + int(cal[2]) == int(cal[4])) or (
            cal[1] == "-" and int(cal[0]) - int(cal[2]) == int(cal[4])
        ):
            answer.append("O")
        else:
            answer.append("X")
    return answer
