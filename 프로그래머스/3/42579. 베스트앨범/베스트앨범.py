def solution(genres, plays):
    dic = {i: [] for i in set(genres)}

    for i in range(len(plays)):
        dic[genres[i]].append(plays[i])

    li = sorted(dic, key=lambda x: -sum(dic[x]))

    temp_li = list((a, b) for a, b in zip(genres, plays))

    answer = []
    for i in li:
        li2 = sorted(dic[i], reverse=True)[:2]
        for j in li2:
            if (i, j) in temp_li:
                answer.append(temp_li.index((i, j)))
                temp_li[temp_li.index((i, j))] = -1
                
    return answer