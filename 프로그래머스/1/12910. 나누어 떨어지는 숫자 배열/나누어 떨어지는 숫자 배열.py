def solution(arr, divisor):
    answer = sorted(list(i for i in arr if not i % divisor))
    return [-1] if not len(answer) else answer