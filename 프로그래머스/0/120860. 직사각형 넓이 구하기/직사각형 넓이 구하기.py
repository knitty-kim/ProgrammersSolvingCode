def solution(dots):
    crit = dots[0]
    dx, dy = 0, 0
    for i in range(1, len(dots)):
        if dots[i][0] == crit[0] and dots[i][1] != crit[1]:
            dy = abs(dots[i][1] - crit[1])
        elif dots[i][0] != crit[0] and dots[i][1] == crit[1]:
            dx = abs(dots[i][0] - crit[0])

    return dx * dy