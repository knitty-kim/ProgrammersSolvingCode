def solution(s):
    stri = s.split()
    return sum([int(stri[i]) if stri[i] != 'Z' else -int(stri[i-1]) for i in range(len(stri))])