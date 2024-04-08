# 삼총사

# https://school.programmers.co.kr/learn/courses/30/lessons/131705


# 재귀함수로 해결하기 
def recur(stk, number, n):
    global answer
    if len(stk) == 3:
        if sum(stk) == 0:
            answer += 1
    else:
        for i in range(n, len(number)):
            stk.append(number[i])
            recur(stk, number, i + 1)
            stk.pop()


answer = 0


def solution(number):
    stk = []
    recur(stk, number, 0)

    return answer

#---------------------------------------------

# 삼중 반복문으로 해결하기
def solution(number):
    answer = 0

    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for k in range(j+1,len(number)):
                if (number[i] + number[j] + number[k]) == 0:
                    answer += 1

    return answer