def solution(s):
    cm = 0
    for v in s:
        if v == '(':
            cm += 1
        elif v == ')':
            cm -= 1
        if cm < 0:
            return False
    return cm == 0