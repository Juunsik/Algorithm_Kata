# [PCCE 기출문제] 6번/가채점

# https://school.programmers.co.kr/learn/courses/30/lessons/250128


def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i] - 1]:
            answer.append("Same")
        else:
            answer.append("Different")

    return answer
