def solution(emergency):
    answer = []
    dic = {e: i+1 for i, e in enumerate(sorted(emergency, reverse=True))}
    for e in emergency:
        answer.append(dic[e])
    return answer