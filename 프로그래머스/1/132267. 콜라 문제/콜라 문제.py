def solution(a, b, n):
    answer = 0
    while n >= a:
        x = b*(n // a)
        y = n % a
        n = x + y
        answer += x
    return answer