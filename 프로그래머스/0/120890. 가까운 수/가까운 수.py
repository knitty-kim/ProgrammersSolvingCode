def solution(array, n):
    arr = list(map(lambda i: abs(n-i), array))
    # min_idx = arr.index(min(arr))
    idx_arr = list(filter(lambda i: arr[i] == min(arr), range(len(arr))))
    # print(idx_arr)
    # print(min(array[i] for i in idx_arr))
    return min(array[i] for i in idx_arr)