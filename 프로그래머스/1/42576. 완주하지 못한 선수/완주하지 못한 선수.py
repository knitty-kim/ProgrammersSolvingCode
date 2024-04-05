def solution(participant, completion):
    dic = {i: 0 for i in participant}
    for i in participant:
        dic[i] += 1
    for i in completion:
        dic[i] -= 1
    return sorted(dic.items(), key=lambda x: -x[1])[0][0]