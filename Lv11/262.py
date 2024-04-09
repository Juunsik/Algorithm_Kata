# 짝지어 제거하기

# https://school.programmers.co.kr/learn/courses/30/lessons/12973


def solution(s):
    stk=[]
    for i in s:
        stk.append(i)
        if len(stk)>=2:
            if stk[-1]==stk[-2]:
                stk.pop()
                stk.pop()
        
    return 0 if stk else 1


# 시간 초과
# def solution(s):
#     length = len(s)
#     for _ in range(length // 2):
#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]:
#                 s = s.replace(s[i] * 2, "")
#                 break

#     return 0 if s else 1