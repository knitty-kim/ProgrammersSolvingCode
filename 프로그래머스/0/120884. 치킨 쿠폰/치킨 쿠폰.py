def solution(chicken):
    service = 0

    # 치킨을 10으로 나눈 몫 = 서비스 받을 수 있는 치킨
    while chicken >= 10:
        service += (chicken // 10)
        n, r = divmod(chicken, 10)
        chicken = n + r

    return service