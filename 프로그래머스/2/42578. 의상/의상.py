def solution(clothes):
    dic = {i[1]: [] for i in clothes}
    for i in clothes:
        dic[i[1]].append(i[0])

    answer = 0
    temp = 1
    for i in dic:
        temp *= len(dic[i]) + 1
    answer += temp
    
    return answer - 1