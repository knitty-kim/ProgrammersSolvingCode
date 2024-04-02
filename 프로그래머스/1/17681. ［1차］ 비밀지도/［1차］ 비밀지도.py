def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        h = bin(i | j)[2:]
        h = h.zfill(n)
        h = h.replace('1', '#')
        h = h.replace('0', ' ')
        answer.append(h)
    return answer