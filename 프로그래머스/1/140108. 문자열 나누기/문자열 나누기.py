def solution(s):
    vari = s[0]
    count = [1, 0]
    slice_count = 0
    flag = False
    for i in range(1, len(s)):
        if flag:
            vari = s[i]
            flag = False
        if vari == s[i]:
            count[0] += 1
        else:
            count[1] += 1
        if count[0] == count[1]:
            slice_count += 1
            flag = True
        else:
            if i == len(s)-1:
                slice_count += 1
    if len(s) == 1:
        slice_count += 1
    return slice_count