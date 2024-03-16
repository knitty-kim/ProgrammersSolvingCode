def solution(n, lost, reserve):
    # 체육복 현황 리스트 초기화
    result = [1] * (n + 2)
    result[0] = -1
    result[n+1] = -1
    
    # 체육복 현황 갱신
    for i in lost:
        result[i] -= 1
    for j in reserve:
        result[j] += 1

    for k in range(1, n+1):
        if result[k-1] == 0 and result[k] == 2:
            result[k] = 1
            result[k-1] = 1
        elif result[k+1] == 0 and result[k] == 2:
            result[k] = 1
            result[k+1] = 1

    return n - result.count(0)