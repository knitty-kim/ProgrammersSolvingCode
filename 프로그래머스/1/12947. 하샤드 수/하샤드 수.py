def solution(x):
    return True if not x % sum(int(i) for i in str(x)) else False