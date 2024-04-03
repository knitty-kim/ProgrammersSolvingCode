def solution(number, limit, power):
    weapons = [0] * number
    for i in range(number):
        knight = i+1
        edge = knight**0.5
        weapon = 0
        for j in range(1, int((edge+1)//1)):
            if j < edge and knight % j == 0:
                weapon += 2
            if j == edge and edge % 1 == 0:
                weapon += 1
        if weapon > limit:
            weapons[i] = power
        else:
            weapons[i] = weapon
    return sum(weapons)