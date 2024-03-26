import heapq
def solution(n):
    heap = []
    for i in str(n):
        heapq.heappush(heap, -int(i))

    li = []
    while heap:
        li.append(-heapq.heappop(heap))
    return int(''.join(str(i) for i in li))