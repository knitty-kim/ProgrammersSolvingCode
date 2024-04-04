def solution(N, stages):
    dic = dict()
    mom = len(stages)
    for i in range(1, N+2):
        if mom == 0:
            dic[i] = 0
        elif mom > 0:
            dic[i] = stages.count(i) / mom
            mom = mom - stages.count(i)
    dic[N+1] = 0
    del dic[N+1]

    pre = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    return [i[0] for i in pre]