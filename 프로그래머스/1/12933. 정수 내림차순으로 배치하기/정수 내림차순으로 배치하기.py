def solution(n):
    return int(''.join(i for i in sorted(list(str(n)), reverse=True)))