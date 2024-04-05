def solution(s, skip, index):
    info = list()
    for i in range(ord('a'), ord('z')+1):
        info.append(chr(i))

    for i in skip:
        info.remove(i)

    answer = ''
    for i in s:
        answer += info[(info.index(i)+index) % len(info)]
    return answer