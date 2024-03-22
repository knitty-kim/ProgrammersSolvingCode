import math
def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    gcd2 = math.gcd(numer, denom)
    return [int(numer // gcd2), int(denom // gcd2)]