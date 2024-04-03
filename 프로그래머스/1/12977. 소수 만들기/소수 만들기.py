from itertools import combinations
def solution(nums):
    count = 0
    for i in list(sum(num) for num in combinations(nums, 3)):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            count += 1
    return count