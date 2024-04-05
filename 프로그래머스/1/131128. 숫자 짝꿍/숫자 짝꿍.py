def solution(X, Y):
    setX = set(X)
    setY = set(Y)
    commonSet = setX & setY

    if len(commonSet) == 0:
        return '-1'

    answer = list()
    for i in commonSet:
        minnum = min(X.count(i), Y.count(i))
        for _ in range(minnum):
            answer.append(i)

    answer.sort(reverse=True)
    if answer[0] == '0':
        return '0'
    else:
        return ''.join(answer)