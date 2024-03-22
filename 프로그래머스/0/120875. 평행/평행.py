def solution(dots):
    dot0 = dots[0]
    dot1 = dots[1]
    dot2 = dots[2]
    dot3 = dots[3]

    grad01 = (dot1[1]-dot0[1]) / (dot1[0]-dot0[0])
    grad02 = (dot2[1]-dot0[1]) / (dot2[0]-dot0[0])
    grad03 = (dot3[1]-dot0[1]) / (dot3[0]-dot0[0])
    grad23 = (dot3[1]-dot2[1]) / (dot3[0]-dot2[0])
    grad13 = (dot3[1]-dot1[1]) / (dot3[0]-dot1[0])
    grad12 = (dot2[1]-dot1[1]) / (dot2[0]-dot1[0])

    if grad01 != grad23 and grad02 != grad13 and grad03 != grad12:
        return 0
    return 1