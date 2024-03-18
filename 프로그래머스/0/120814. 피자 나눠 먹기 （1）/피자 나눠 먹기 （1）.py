def solution(n):
    answer = n // 7
    if 1 <= n % 7 < 7:
        answer += 1
    return answer