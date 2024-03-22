def solution(num, total):
    a1 = int(total // num - (num - 1) // 2)
    print(a1)
    return sorted([i for i in range(a1, a1+(num-1)+1)])