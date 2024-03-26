def solution(num):
    if num == 1:
        return 0

    cnt = 0
    while True:
        if num == 1:
            return cnt
        if cnt == 501:
            return -1
        if num % 2 == 0:
            num //= 2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1