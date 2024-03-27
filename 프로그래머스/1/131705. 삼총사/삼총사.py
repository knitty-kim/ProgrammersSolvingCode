from itertools import combinations
def solution(number):
    return sum(1 for i in list(combinations(number, 3)) if sum(i) == 0)