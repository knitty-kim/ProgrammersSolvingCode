import math
def solution(a, b):
    # 최대공약수 c
    c = math.gcd(a, b)
    while a % c == 0 and b % c == 0 and c != 1:
        a //= c
        b //= c

    while True:
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            break

    if b != 1:
        return 2
    else:
        return 1