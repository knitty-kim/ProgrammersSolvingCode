def solution(s):
    count = [0, 0]
    slice = 0
    for i in range(len(s)):
        if count[0] == count[1]:
            slice += 1
            vari = s[i]
        if vari == s[i]:
            count[0] += 1
        else:
            count[1] += 1
    return slice