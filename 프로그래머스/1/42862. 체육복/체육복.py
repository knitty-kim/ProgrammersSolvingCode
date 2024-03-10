def solution(n, lost, reserve):

    lost.sort()
    reserve.sort()

    # 공통 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 체육복 빌려주기
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    return n - len(lost)