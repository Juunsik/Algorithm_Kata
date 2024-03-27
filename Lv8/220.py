# 수열과 구간 쿼리 2

# https://school.programmers.co.kr/learn/courses/30/lessons/181923


def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        print(s, e, k)
        temp = [i for i in arr[s : e + 1] if i > k]
        answer.append(min(temp) if temp else -1)

    return answer
