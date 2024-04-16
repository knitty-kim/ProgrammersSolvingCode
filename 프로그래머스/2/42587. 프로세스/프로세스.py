def solution(priorities, location):
    tempArr = [(i, v) for i, v in enumerate(priorities)]
    lastArr = []
    maxN = max(i[1] for i in tempArr)
    while len(tempArr) > 0:
        p = tempArr.pop(0)
        if p[1] < maxN:
            tempArr.append(p)
        elif p[1] == maxN:
            lastArr.append(p)
            if tempArr:
                maxN = max(i[1] for i in tempArr)

    return lastArr.index((location, priorities[location])) + 1