def solution(k, score):
    answer = []
    li = list()
    for i in score:
        li.append(i)
        li.sort(reverse=True)
        li = li[:k]
        answer.append(li[-1])
    return answer