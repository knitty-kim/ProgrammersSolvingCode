from itertools import combinations
def solution(numbers):
    return sorted(list(set(i[0]+i[1] for i in set(combinations(numbers, 2)))))