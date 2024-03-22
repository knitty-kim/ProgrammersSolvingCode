def solution(common):
    d1 = abs(common[1]-common[0])
    d2 = abs(common[2]-common[1])

    if d1 == d2:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] // common[0])