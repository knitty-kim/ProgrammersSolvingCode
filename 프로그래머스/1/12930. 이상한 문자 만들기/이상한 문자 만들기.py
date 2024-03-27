def solution(s):
    li = list(s.split(' '))
    for i in range(len(li)):
        tmp_li = list(li[i])
        for j in range(len(tmp_li)):
            if j % 2:
                tmp_li[j] = tmp_li[j].lower()
            else:
                tmp_li[j] = tmp_li[j].upper()
        li[i] = ''.join(tmp_li)
    return ' '.join(li)