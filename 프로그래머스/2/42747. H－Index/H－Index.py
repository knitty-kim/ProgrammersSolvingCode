def solution(citations):
    citations.sort()

    arr = []
    h = 0
    while True:
        cnt = 0
        for i in citations:
            if i >= h:
                cnt += 1
        if cnt >= h:
            arr.append(h)
        h += 1
        if h > len(citations):
            break
            
    return max(arr)