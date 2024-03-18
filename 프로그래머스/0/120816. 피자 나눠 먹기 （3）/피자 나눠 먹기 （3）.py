def solution(slice, n):
    a = n // slice
    b = n % slice
    if 0 < b:
        a += 1
    return a