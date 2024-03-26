def solution(price, money, count):
    result = sum(price*i for i in range(1, count+1))
    return result - money if result > money else 0