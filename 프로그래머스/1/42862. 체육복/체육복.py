def solution(n, lost, reserve):
    real_reser = [r for r in reserve if r not in lost]
    real_lost = [l for l in lost if l not in reserve]
    real_reser.sort()
    real_lost.sort()
    for r in real_reser:
        f = r - 1
        b = r + 1
        if f in real_lost:
            real_lost.remove(f)
        elif b in real_lost:
            real_lost.remove(b)
    return n - len(real_lost)