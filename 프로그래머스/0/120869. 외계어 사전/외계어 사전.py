def solution(spell, dic):
    length = [0] * len(dic)
    for j in spell:
        for i in dic:
            if i.count(j) == 1:
                length[dic.index(i)] += 1

    for k in length:
        if k == len(spell):
            return 1
    return 2