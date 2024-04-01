# 치킨 쿠폰

# https://school.programmers.co.kr/learn/courses/30/lessons/120884


def solution(chicken):
    chicken = str(chicken)
    result = 0
    coupon = 0
    for _ in range(len(chicken) - 1):
        result += int(chicken[:-1])
        coupon += int(chicken[-1])
        chicken = chicken[:-1]

    coupon = int(chicken) + coupon
    while coupon >= 10:
        result += coupon // 10
        coupon = coupon // 10 + coupon % 10

    return result
