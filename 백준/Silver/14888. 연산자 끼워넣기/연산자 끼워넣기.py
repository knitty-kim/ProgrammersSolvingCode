# 연산자 끼워 넣기

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = 1e9
max_val = -1e9

def recursive(total, i, add, sub, mul, div):
    global max_val, min_val, data, n
    if i == n:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return
    else:
        if add != 0:
            recursive(total + data[i], i+1, add-1, sub, mul, div)
        if sub != 0:
            recursive(total - data[i], i+1, add, sub-1, mul, div)
        if mul != 0:
            recursive(total * data[i], i+1, add, sub, mul-1, div)
        if div != 0:
            recursive(int(total / data[i]), i+1, add, sub, mul, div-1)

recursive(data[0], 1, add, sub, mul, div)

print(int(max_val))
print(int(min_val))