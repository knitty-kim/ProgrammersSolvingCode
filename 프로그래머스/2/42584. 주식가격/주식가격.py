def solution(prices):
    stocks = [[i, 0] for i in prices]
    for j in range(len(stocks)):
        for i in range(j+1, len(prices)):
            if stocks[j][0] <= prices[i]:
                stocks[j][1] += 1
            else:
                stocks[j][1] += 1
                break
    answer = [i[1] for i in stocks]
    return answer