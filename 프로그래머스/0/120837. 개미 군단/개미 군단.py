def solution(hp):
    answer = 0
    n, hp = divmod(hp, 5)
    answer += n
    n, hp = divmod(hp, 3)
    answer += n + hp
    return answer