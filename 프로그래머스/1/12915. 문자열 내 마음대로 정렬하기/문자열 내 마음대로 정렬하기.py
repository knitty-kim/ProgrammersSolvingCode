def solution(strings, n):
    dic = {v: v[n] for i, v in enumerate(strings)}
    li = sorted(dic.items(), key=lambda x: (x[1], x[0]))
    answer = list(i[0] for i in li)
    return answer