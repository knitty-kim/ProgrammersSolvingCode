# 연산자 끼워 넣기
# from itertools import product
# n = 4
# print(list(product(['+', '-', '*', '/'], repeat=(n-1))))

# 0. 입력 받기
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최소값과 최대값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(int(max_value))
print(int(min_value))
