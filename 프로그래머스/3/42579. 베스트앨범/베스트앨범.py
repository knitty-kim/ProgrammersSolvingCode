def solution(genres, plays):
    dic = {i: [] for i in set(genres)}

    for i in range(len(plays)):
        dic[genres[i]].append(plays[i])

    zip_li = list((a, b) for a, b in zip(genres, plays))

    answer = []
    for i in sorted(dic, key=lambda x: -sum(dic[x])):
        for j in sorted(dic[i], reverse=True)[:2]:
            if (i, j) in zip_li:
                answer.append(zip_li.index((i, j)))
                zip_li[zip_li.index((i, j))] = -1

    return answer