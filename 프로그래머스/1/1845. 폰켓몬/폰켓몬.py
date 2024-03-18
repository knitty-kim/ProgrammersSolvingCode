import copy
def solution(nums):
    set1 = set()
    max_num = len(nums) // 2
    answer = 0

    for num in nums:
        set1.add(num)

    temp_set = copy.deepcopy(set1)

    for pokemon in temp_set:
        if answer == max_num:
            break
        set1.remove(pokemon)
        answer += 1

    return answer