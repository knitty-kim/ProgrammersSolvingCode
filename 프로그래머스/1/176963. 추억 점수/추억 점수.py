def solution(name, yearning, photo):
    info = dict(zip(name, yearning))
    answer = []
    for i in photo:
        score = 0
        for j in i:
            if j in info:
                score += info.get(j)
        answer.append(score)
    return answer