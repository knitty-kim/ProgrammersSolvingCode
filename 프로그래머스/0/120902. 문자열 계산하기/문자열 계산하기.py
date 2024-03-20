def solution(my_string):
    arr = my_string.split()
    return int(arr[0]) + sum(int(arr[i+1]) if arr[i] == '+' else -int(arr[i+1]) for i in range(1, len(arr), 2))