def solution(balls, share):
    perm = 1
    count = 0
    for i in range(balls, 0, -1):
        if count == share:
            break
        perm *= i
        count += 1

    facto = 1
    for j in range(share, 0, -1):
        facto *= j

    return int(perm / facto)