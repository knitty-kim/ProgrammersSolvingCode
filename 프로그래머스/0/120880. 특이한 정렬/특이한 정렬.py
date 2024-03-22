def solution(numlist, n):

    dic = {v: v-n for i, v in enumerate(numlist)}
    result = sorted(dic.items(), key=lambda i: abs(i[1]))
    for i in range(len(result)):
        if abs(result[i-1][1]) == abs(result[i][1]) and result[i-1][1] < 0:
            result[i], result[i-1] = result[i-1], result[i]
    answer = [item[0] for item in result]
    return answer