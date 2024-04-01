# 대소문자 바꿔서 출력하기

# https://school.programmers.co.kr/learn/courses/30/lessons/181949

str = input()
answer = ""
for i in str:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()

print(answer)
