def solution(hp):
    answer = 0
    n, r = divmod(hp, 5)
    answer += n
    hp = r
    n, r = divmod(hp, 3)
    answer += n
    hp = r
    n = hp // 1
    answer += n
    return answer