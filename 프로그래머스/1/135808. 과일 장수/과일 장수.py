def solution(k, m, score):
    score.sort(reverse=True)
    total = 0
    for i in range(0, len(score), m):
        box = score[i:i+m]
        if len(box) == m:
            min_apple = min(box)
            total += min_apple * m
    return total