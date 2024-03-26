def solution(x, n):

    answer = []
    d = x
    answer.append(x)
    for i in range(n-1):
        x += d
        answer.append(x)
    return answer