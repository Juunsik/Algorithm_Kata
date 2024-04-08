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


print(solution([-2, 3, 0, 2, -5]))
