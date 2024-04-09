def solution(players, callings):
    dic1 = {v: i for i, v in enumerate(players)}
    dic2 = {i: v for i, v in enumerate(players)}

    for called in callings:
        prior = dic2[dic1[called]-1]
        dic1[called] -= 1
        dic1[prior] += 1
        dic2[dic1[called]] = called
        dic2[dic1[prior]] = prior

    return sorted(dic1, key=lambda x: dic1[x])