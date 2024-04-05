def solution(n, lost, reserve):
    reserved = 0
    lost_li = list(set(lost) - set(reserve))
    rsve_li = list(set(reserve) - set(lost))
    lost_li.sort()
    rsve_li.sort()
    for i in lost_li:
        for x in range(i-1, i+2):
            if x in rsve_li:
                rsve_li.remove(x)
                reserved += 1
                break
    return n + reserved - len(lost_li)