def solution(n):
    return len([i for i in range(4, n+1) if not all(i % j for j in range(2, int(i ** 0.5)+1))])