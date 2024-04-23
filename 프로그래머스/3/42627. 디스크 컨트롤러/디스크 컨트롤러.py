import heapq
def solution(jobs):
    # 갖고 있는 데이터
    # - 요청 시점, 작업 경과 시간
    # 만들 데이터
    # - 작업완료시간

    # 1. jobs 순회
    # 2. 종료-요청이 작은 작업 먼저
    # -> 특정 기준으로 정렬이 되어있어야 하나?
    # -> 남은 jobs 순회하면서 if 조건에 따라 pop
    heapq.heapify(jobs)
    answer, done_time, count = 0, 0, 0
    start = -1
    heap = []

    while count < len(jobs):
        # jobs 순회하며 heap 구성
        for job in jobs:
            # 이전 작업 진행중 요청이 들어온 job들에 대해 heap 구성
            if start < job[0] <= done_time:
                heapq.heappush(heap, [job[1], job[0]])

        # heap이 빈값이 아니라면, heappop
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = done_time           # 작업시작 시간 세팅
            done_time += current[0]     # 작업경과 시간 세팅
            answer += (done_time - current[1])      # 종료-요청 시간 구성
            count += 1

        # heap이 빈값이라면,
        else:
            done_time += 1

    return int(answer/len(jobs))