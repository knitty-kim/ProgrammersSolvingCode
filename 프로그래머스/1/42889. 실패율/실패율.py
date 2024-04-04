def solution(N, stages):
    dic = dict()
    mom = len(stages)
    for i in range(1, N+1):
        if mom == 0:
            dic[i] = 0
        elif mom > 0:
            dic[i] = stages.count(i) / mom
            mom -= stages.count(i)

    pre = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    return [i[0] for i in pre]