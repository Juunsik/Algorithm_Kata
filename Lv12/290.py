# 괄호 회전하기

# https://school.programmers.co.kr/learn/courses/30/lessons/76502


def equal_cnt(s):
    if (
        (s.count("(") == s.count(")"))
        and (s.count("{") == s.count("}"))
        and (s.count("[") == s.count("]"))
    ):
        return True
    return False


def solution(s):
    answer = 0
    if equal_cnt(s):
        for i in range(len(s)):
            text = s[-i:] + s[:-i]
            stack = []
            for j in text:
                if stack and j == stack[-1]:
                    stack.pop()
                else:
                    if j == "{":
                        stack.append("}")
                    elif j == "[":
                        stack.append("]")
                    elif j == "(":
                        stack.append(")")
            if not stack:
                answer += 1

    return answer
