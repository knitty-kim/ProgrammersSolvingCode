def solution(array):
    dic = {v: array.count(v) for i, v in enumerate(array)}
    result = sorted(dic.items(), key=lambda i: -i[1])

    max_cnt = result[0][1]
    for i in range(1, len(result)):
        if result[i][1] == max_cnt:
            return -1
    return result[0][0]