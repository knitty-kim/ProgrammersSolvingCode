def solution(s):
    answer = True

    arr = []
    for i in range(len(s)):
        if i == 0:
            if s[i] == '(':
                arr.append(s[i])
            else:
                return False
        else:
            arr.append(s[i])
            if arr[-2:] == ['(', ')']:
                arr.pop()
                arr.pop()

    if len(arr) != 0:
        return False
    else:
        return True