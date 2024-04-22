import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    for i in range(len(scoville)):
        if scoville[0] >= K:
            return cnt
        elif len(scoville) == 1 and scoville[0] < K:
            return -1
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        a = f + s*2
        heapq.heappush(scoville, a)
        cnt += 1