def solution(n, lost, reserve):
    dic = {i: 1 for i in range(1, n+1)}
    for i in reserve:
        dic[i] += 1
    for i in lost:
        dic[i] -= 1

    for key in dic.keys():
        if dic[key] == 2 and key-1 in dic:
            if dic[key-1] == 0:
                dic[key] -= 1
                dic[key-1] += 1
        if dic[key] == 2 and key+1 in dic:
            if dic[key+1] == 0:
                dic[key] -= 1
                dic[key+1] += 1
                
    return sum(1 for i in dic.values() if i > 0)