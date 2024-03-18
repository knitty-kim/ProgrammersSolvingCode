def solution(n, lost, reserve):
    new_reserve = [r for r in reserve if r not in lost]
    new_lost = [l for l in lost if l not in reserve]
    
    new_lost.sort()
    new_reserve.sort()
    
    for r in new_reserve:
        foward = r - 1
        backward = r + 1
        if foward in new_lost:
            new_lost.remove(foward)
        elif backward in new_lost:
            new_lost.remove(backward)

    return (n - len(new_lost))