def solution(n):
    # 10진법은 idx
    # my_set = set(i for i in range(1, 501) if i % 3 == 0 or str(i).count('3'))
    # li = [i for i in range(1, 501)]

    result2 = [i for i in range(1, 601) if i % 3 != 0 and not str(i).count('3')]

    return result2[n-1]