def solution(s):
    arr = []
    for i in s:
        if i == '(':
            arr.append(i)
        elif i == ')':
            if arr:
                arr.pop()
            else:
                return False
    return len(arr) == 0