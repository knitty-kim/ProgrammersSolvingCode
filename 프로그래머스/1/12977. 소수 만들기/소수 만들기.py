from itertools import combinations
def solution(nums):
    count = 0
    li = list(sum(i) for i in combinations(nums, 3))
    for i in li:
        flag = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            count += 1
    return count