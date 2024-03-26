def solution(n, m):
    gcnum = max(i for i in range(1, min(n, m)+1) if n%i == 0 and m%i ==0)
    # lcnum = min(i for i in range(min(n, m), n*m+1) if i%n == 0 and i%m == 0)
    return [gcnum, int(n*m/gcnum)]