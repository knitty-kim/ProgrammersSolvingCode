def solution(i, j, k):
    li = list(str(x) for x in range(i, j+1))
    return sum(y.count(str(k)) for y in li if y.find(str(k)) != -1)