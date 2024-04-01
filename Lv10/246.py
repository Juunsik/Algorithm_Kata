# 이상한 문자 만들기

# https://school.programmers.co.kr/learn/courses/30/lessons/12930


def solution(s):
    answer = []
    temp = ""
    for i in s.split(" "):  # 공백이 한번에 여러개일 수 있어서 기준 공백 하나로 나눔
        for j in range(len(i)):
            if j % 2 == 0:
                temp += i[j].upper()
            else:
                temp += i[j].lower()
        answer.append(temp)
        temp = ""
    return " ".join(answer)
