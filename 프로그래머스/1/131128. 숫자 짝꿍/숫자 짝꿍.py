from collections import Counter
def solution(X, Y):
    cntX = Counter(list(X))
    cntY = Counter(list(Y))

    commonSet = set(X) & set(Y)
    if len(commonSet) == 0:
        return '-1'

    commonLi = list(commonSet)
    commonLi.sort(reverse=True)

    answer = ''
    for i in commonLi:
        minnum = min(cntX[i], cntY[i])
        for _ in range(minnum):
            answer += i

    if answer[0] == '0':
        return '0'
    else:
        return answer