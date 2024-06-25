import heapq
def solution(food_times, k):
    # k가 모두 먹는 시간 이상이면 -1
    if k >= sum(food_times):
        return -1

    # 우선순위 큐에 삽입
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0   # 총 먹은 시간
    prev = 0    # 직전에 다 먹은 음식 시간
    length = len(food_times)    # 남은 음식의 개수

    while sum_value + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - prev) * length
        length -= 1     # 다 먹은 음식 큐에서 제거
        prev = now      # 다음 순회에서의 이전 음식이 갱신

    result = sorted(q, key=lambda x: x[1])      # 음식 번호 기준 정렬
    return result[(k - sum_value) % length][1]