def solution(n, m, section):
    milestone = section[0]
    count = 1
    for i in section:
        if milestone + (m-1) < i:
            milestone = i
            count += 1
    return count