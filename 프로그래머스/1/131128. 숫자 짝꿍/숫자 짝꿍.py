def solution(X, Y):
    setX = set(X)
    setY = set(Y)
    commonSet = setX & setY

    if len(commonSet) == 0:
        return '-1'

    commonLi = list(commonSet)
    commonLi.sort(reverse=True)

    answer = ''
    for i in commonLi:
        minnum = min(X.count(i), Y.count(i))
        for _ in range(minnum):
            answer += i

    if answer[0] == '0':
        return '0'
    else:
        return answer