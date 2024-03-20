def solution(n):
    arr = [i for i in range(1, n+1) if n % i == 0]
    temp_set = set()
    for j in range(1, len(arr)-1):
        for k in range(j+1, len(arr)):
            if arr[k] % arr[j] == 0:
                temp_set.add(arr[k])
    for i in temp_set:
        if i in arr:
            arr.remove(i)
    arr.remove(1)
    return arr