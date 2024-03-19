def solution(age):
    return ''.join(list(map(lambda i: chr(i + 97), [int(i) for i in str(age)])))