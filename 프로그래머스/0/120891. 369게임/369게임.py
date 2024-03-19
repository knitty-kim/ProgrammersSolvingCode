def solution(order):
    stri = list(str(order))
    count = 0
    for i in stri:
        if int(i) % 3 == 0 and int(i) != 0:
            count += 1
    return count