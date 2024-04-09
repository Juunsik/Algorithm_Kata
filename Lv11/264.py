# 카펫

# https://docs.google.com/spreadsheets/d/1TRBYs9WXz61xoW3ACeklombx8KZqaTekqwuCS5eyiIU/edit#gid=1386063159


def solution(brown, yellow):
    divisor = []
    total = brown + yellow

    for i in range(1, int(total ** (1 / 2)) + 1):
        if total % i == 0:
            if (i**2) != total:
                divisor.append([total // i, i])
            else:
                divisor.append([i, i])
    divisor.sort()

    for i in divisor:
        if yellow == (i[0] - 2) * (i[1] - 2):
            return i
    return None
