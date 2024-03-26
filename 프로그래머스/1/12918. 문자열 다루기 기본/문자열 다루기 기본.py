def solution(s):
    return all(True if i.isdigit() else False for i in s) and (len(s) == 4 or len(s) == 6)