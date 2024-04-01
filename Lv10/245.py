# 숫자의 표현

# https://school.programmers.co.kr/learn/courses/30/lessons/12924

# a + (a+1) + (a+2) + ... + (a+k-1) = k(2a+k-1)/2 = n
# a = n/k + (1-k)/2
# k는 n의 약수
# 1-k 가 짝수여야 하므로 k는 홀수


def solution(n):
    answer = 0
    for i in range(1, n + 1, 2):
        if n % i == 0:
            answer += 1
    return answer
